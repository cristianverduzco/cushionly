from fastapi import FastAPI

from app.core.database import engine, Base
from app.models import user, budget, expense  # Ensure all models are imported
from app.routes import auth, budget as budget_routes

app = FastAPI()

# 👇 Create all tables at startup (for development only)
Base.metadata.create_all(bind=engine)

# 👇 Register routers
app.include_router(auth.router)
app.include_router(budget_routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Cushionly Backend!"}
