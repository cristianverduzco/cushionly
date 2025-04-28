from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    total_amount = Column(Float, nullable=False)  # 🔥 CHANGED from limit ➔ total_amount
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="budgets")
    expenses = relationship("Expense", back_populates="budget", cascade="all, delete")
