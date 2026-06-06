from fastapi import FastAPI
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select

app = FastAPI()

class Expense(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    ammount: float
    category: str


engine = create_engine("sqlite:///database.db", connect_args= {"check_same_thread": False})

def init_db():
    SQLModel.metadata.create_all(engine)

init_db() 

@app.post("/expensive/")
def add_expensive(expensive: Expense):
    
    with Session(engine) as session:
        session.add(expensive)
        session.commit()
        session.refresh(expensive)

    return {"message": "Spesa aggiunta con successo!", "data": expensive}

@app.get("/expensive/")
def get_all_expensive():

    with Session(engine) as session:
        statement = select(Expense)
        result = session.exec(statement).all()
        return result

@app.get("/")
def read_root():
    return {"message": "Welcome to your personal expenses tracker"}
