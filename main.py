from fastapi import FastAPI
from contextlib import asynccontextmanager

from database import init_db
from api.auth_router import router as auth_router
from api.user_router import router as user_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
    
app = FastAPI(title="Expense Tracker", lifespan= lifespan)

app.include_router(auth_router)
app.include_router(user_router)

@app.get("/")
def read_root():
   return {"message": "Welcome to your personal expenses tracker"} 
