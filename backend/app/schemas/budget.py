from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# --- Expenses ---

class ExpenseBase(BaseModel):
    name: str
    amount: float

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseOut(ExpenseBase):
    id: int
    date: datetime  # Optional: use datetime instead of str for date field

    class Config:
        from_attributes = True

# --- Budgets ---

class BudgetBase(BaseModel):
    name: str
    total_amount: float  # Changed from limit ➔ total_amount

class BudgetCreate(BudgetBase):
    pass

class BudgetOut(BudgetBase):
    id: int
    expenses: List[ExpenseOut] = []

    class Config:
        from_attributes = True
