from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models.budget import Budget
from app.models.expense import Expense
from app.schemas.budget import BudgetCreate, BudgetOut, ExpenseCreate, ExpenseOut
from app.core.security import get_current_user
from app.models.user import User
from app.schemas.budget import BudgetCreate, BudgetOut, ExpenseCreate, ExpenseOut


router = APIRouter(
    prefix="/budgets",
    tags=["budgets"]
)

@router.post("/", response_model=BudgetOut)
def create_budget(budget: BudgetCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_budget = Budget(
        name=budget.name,
        total_amount=budget.total_amount,
        owner_id=current_user.id
    )
    db.add(db_budget)
    db.commit()
    db.refresh(db_budget)

    total_spent = 0
    remaining_amount = db_budget.total_amount

    return BudgetOut(
        id=db_budget.id,
        name=db_budget.name,
        total_amount=db_budget.total_amount,
        total_spent=total_spent,
        remaining_amount=remaining_amount,
        expenses=[]
    )

@router.get("/", response_model=List[BudgetOut])
def get_budgets(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    budgets = db.query(Budget).filter(Budget.owner_id == current_user.id).all()

    budget_list = []
    for budget in budgets:
        total_spent = sum(expense.amount for expense in budget.expenses)
        remaining_amount = budget.total_amount - total_spent

        budget_list.append(BudgetOut(
            id=budget.id,
            name=budget.name,
            total_amount=budget.total_amount,
            total_spent=total_spent,
            remaining_amount=remaining_amount,
            expenses=budget.expenses
        ))

    return budget_list

@router.post("/{budget_id}/expenses", response_model=ExpenseOut)
def add_expense(budget_id: int, expense: ExpenseCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
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

@router.get("/{budget_id}/expenses", response_model=List[ExpenseOut])
def get_expenses(budget_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    budget = db.query(Budget).filter(Budget.id == budget_id, Budget.owner_id == current_user.id).first()
    if not budget:
        raise HTTPException(status_code=404, detail="Budget not found")

    return budget.expenses
