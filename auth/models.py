from datetime import datetime
from sqlmodel import Field, SQLModel

class Credential(SQLModel, table= True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique= True, index= True)
    hashed_password: str

class Token(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    token: str = Field(unique=True, index=True)
    expired_date: datetime
    credential_id: int = Field(unique=True, index=True)

