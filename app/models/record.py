from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from app.database import Base

class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    type = Column(String, nullable=False)  # income / expense
    category = Column(String)
    date = Column(Date)
    notes = Column(String)

    owner_id = Column(Integer, ForeignKey("users.id"))