from fastapi import FastAPI
from contextlib import asynccontextmanager

from database import init_db
from api.auth_routher import router as auth_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
    
app = FastAPI(title="Expense Tracker", lifespan= lifespan)

app.include_router(auth_router)

@app.get("/")
def read_root():
   return {"message": "Welcome to your personal expenses tracker"} 
