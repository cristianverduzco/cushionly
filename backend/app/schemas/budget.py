from pydantic import BaseModel
from typing import List
from datetime import datetime

# --- Expenses ---

class ExpenseBase(BaseModel):
    name: str
    amount: float

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseOut(ExpenseBase):
    id: int
    date: datetime

    class Config:
        from_attributes = True

# --- Budgets ---

class BudgetOut(BaseModel):
    id: int
    name: str
    total_amount: float
    total_spent: float
    remaining_amount: float
    expenses: List[ExpenseOut] = []

    class Config:
        from_attributes = True

class BudgetCreate(BaseModel):
    name: str
    total_amount: float
