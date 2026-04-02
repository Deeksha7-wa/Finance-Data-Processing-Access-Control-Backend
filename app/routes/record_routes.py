from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from datetime import date

from app.database import SessionLocal
from app.models.record import Record
from app.schemas.record_schema import RecordCreate
from app.core.role_checker import role_required

router = APIRouter()

# DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE (Admin only)
@router.post("/")
def create_record(
    record: RecordCreate,
    db: Session = Depends(get_db),
    user = Depends(role_required(["admin"]))
):
    new_record = Record(**record.dict(), owner_id=user.id)
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record


# READ (All roles)
@router.get("/")
def get_records(
    db: Session = Depends(get_db),
    user = Depends(role_required(["admin", "analyst", "viewer"])),
    category: Optional[str] = Query(None),
    type: Optional[str] = Query(None),
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None)
):
    query = db.query(Record)

    if category:
        query = query.filter(Record.category == category)

    if type:
        query = query.filter(Record.type == type)

    if start_date:
        query = query.filter(Record.date >= start_date)

    if end_date:
        query = query.filter(Record.date <= end_date)

    return query.all()


# UPDATE (Admin only)
@router.put("/{record_id}")
def update_record(
    record_id: int,
    updated: RecordCreate,
    db: Session = Depends(get_db),
    user = Depends(role_required(["admin"]))
):
    record = db.query(Record).filter(Record.id == record_id).first()

    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    for key, value in updated.dict().items():
        setattr(record, key, value)

    db.commit()
    return {"message": "Updated successfully"}


# DELETE (Admin only)
@router.delete("/{record_id}")
def delete_record(
    record_id: int,
    db: Session = Depends(get_db),
    user = Depends(role_required(["admin"]))
):
    record = db.query(Record).filter(Record.id == record_id).first()

    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    db.delete(record)
    db.commit()

    return {"message": "Deleted successfully"}
# SUMMARY
@router.get("/summary")
def summary(
    db: Session = Depends(get_db),
    user = Depends(role_required(["admin", "analyst"]))
):
    records = db.query(Record).all()

    total_income = sum(r.amount for r in records if r.type == "income")
    total_expense = sum(r.amount for r in records if r.type == "expense")

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": total_income - total_expense
    }