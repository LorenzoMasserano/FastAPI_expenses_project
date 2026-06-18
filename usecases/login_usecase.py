from sqlmodel import Session
from auth.schemas import LoginRequest, TokenResponse
import auth.service as auth_service
from fastapi import HTTPException, status
from config import settings

auth_error = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

def start_login_flow(session: Session, login_request: LoginRequest) -> TokenResponse:

    id = get_credential_id(session=session, login_request=login_request)

    access_token = auth_service.generate_jwt(credential_id=id, secret_key=settings.SECRET_KEY) 
    
    return TokenResponse(
        token= access_token
    )

def get_credential_id(session: Session, login_request: LoginRequest) -> int: 

    credential = auth_service.login(session=session, login_request=login_request)

    if credential == None or credential.id == None:
         raise auth_error 

    return credential.id

