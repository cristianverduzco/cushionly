from fastapi import FastAPI
from app.routes import auth
from app.core.database import engine, Base
from app.models import user
from app.routes import auth, budget

app = FastAPI()

# Create database tables (for dev purposes only)
Base.metadata.create_all(bind=engine)

# Include your routes
app.include_router(auth.router)
app.include_router(budget.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to Cushionly Backend!"}
