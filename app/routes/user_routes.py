from fastapi import APIRouter, Depends
from app.core.role_checker import role_required

router = APIRouter()

# Admin only
@router.get("/admin-only")
def admin_data(user = Depends(role_required(["admin"]))):
    return {"message": f"Welcome Admin {user.username}!"}

# Analyst + Admin
@router.get("/analytics")
def analytics_data(user = Depends(role_required(["admin", "analyst"]))):
    return {"message": f"Analytics data for {user.username}"}

# Viewer + Analyst + Admin
@router.get("/dashboard")
def dashboard(user = Depends(role_required(["admin", "analyst", "viewer"]))):
    return {"message": f"Dashboard for {user.username}"}