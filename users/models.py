from datetime import datetime, timezone
from sqlmodel import SQLModel, Field

class UserData(SQLModel, table= True):
    id: int | None = Field(default= None, primary_key= True)
    credential_id: int = Field(unique= True, index= True)

    first_name: str
    last_name: str
    avatar_url: str | None = None

    create_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
