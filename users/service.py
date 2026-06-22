from pydantic import EmailStr
from sqlmodel import Session, select
from users.models import UserData

def get_user_data(session: Session, credential_id: int) -> UserData | None:
    statement = select(UserData).where(UserData.credential_id== credential_id)
    return session.exec(statement).first()

def register_user_date(session: Session, credential_id: int, first_name: str, last_name: str, email: EmailStr) -> UserData | None:
    user_data = UserData(
        credential_id=credential_id,
        first_name=first_name,
        last_name=last_name,
        email=email
    )

    session.add(user_data)
    session.flush()
    session.refresh(user_data)
    session.commit()
    return user_data
 
def is_email_already_used(session: Session, email: str) -> bool:
    statement= select(UserData).where(UserData.email == email)
    result= session.exec(statement).first

    return result == True   
