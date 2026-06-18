from sqlmodel import Session, select
from users.models import UserData

def get_user_data(session: Session, credential_id: int) -> UserData | None:
    statement = select(UserData).where(UserData.credential_id== credential_id)
    return session.exec(statement).first()
