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

class BudgetBase(BaseModel):
    name: str
    total_amount: float

class BudgetCreate(BudgetBase):
    pass

class BudgetOut(BudgetBase):
    id: int
    created_at: datetime
    expenses: List[ExpenseOut] = []

    # Auto-calculated fields
    total_spent: float
    remaining: float

    class Config:
        from_attributes = True
