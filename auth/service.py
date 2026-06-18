import jwt
from datetime import datetime, timedelta, timezone
    
from sqlmodel import Session, select

from .models import Credential
from .schemas import LoginRequest
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated= "auto")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def login(session: Session, login_request: LoginRequest) -> Credential | None:
    credential = get_user_credential_db(session, login_request)

    if credential == None or not verify_password(hashed_password= credential.hashed_password, plain_password= login_request.password):
        return None

    return credential

def get_user_credential_db(session:Session, login_request: LoginRequest) -> Credential | None:
    statement = select(Credential).where(Credential.username == login_request.useranme)
    return session.exec(statement).first()


def verify_password(hashed_password: str, plain_password: str) -> bool: 
    return pwd_context.verify(plain_password, hashed_password)

def generate_jwt(credential_id: int, secret_key: str, expires_delta: timedelta | None = None) -> str:

    delta = expires_delta if expires_delta else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expied_date = calculate_expired_date(expires_delta= delta)

    to_encode = {
        "sub": str(credential_id),
        "exp": expied_date
    }

    return jwt.encode(
        to_encode,
        secret_key,
        ALGORITHM
    )

def calculate_expired_date(expires_delta: timedelta) -> datetime:
    return datetime.now(timezone.utc) + expires_delta
