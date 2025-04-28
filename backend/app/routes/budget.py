from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models.budget import Budget
from app.models.expense import Expense
from app.schemas.budget import BudgetCreate, BudgetOut, ExpenseCreate, ExpenseOut
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/budgets",   # already included, no need to repeat "/budgets" in paths
    tags=["budgets"]
)

# --- Create Budget ---
@router.post("/", response_model=BudgetOut)
def create_budget(
    budget: BudgetCreate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    db_budget = Budget(
        name=budget.name,
        total_amount=budget.total_amount,
        owner_id=current_user.id  # 💬 fixed to owner_id
    )
    db.add(db_budget)
    db.commit()
    db.refresh(db_budget)
    return db_budget

# --- Get All Budgets for Current User ---
@router.get("/", response_model=List[BudgetOut])
def get_budgets(
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    budgets = db.query(Budget).filter(Budget.owner_id == current_user.id).all()
    return budgets

# --- Add Expense to a Budget ---
@router.post("/{budget_id}/expenses", response_model=ExpenseOut)
def add_expense(
    budget_id: int,
    expense: ExpenseCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    budget = db.query(Budget).filter(Budget.id == budget_id, Budget.owner_id == current_user.id).first()
    if not budget:
        raise HTTPException(status_code=404, detail="Budget not found")

    new_expense = Expense(
        name=expense.name,
        amount=expense.amount,
        budget_id=budget.id
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

# --- Get Expenses for a Budget ---
@router.get("/{budget_id}/expenses", response_model=List[ExpenseOut])
def get_expenses(
    budget_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    budget = db.query(Budget).filter(Budget.id == budget_id, Budget.owner_id == current_user.id).first()
    if not budget:
        raise HTTPException(status_code=404, detail="Budget not found")

    return budget.expenses
