from fastapi import APIRouter, Depends
from sqlmodel import Session

from api.schemas import RegistrationRequest
from auth.schemas import LoginRequest, TokenResponse
from database import get_session
from usecases.login_usecase import start_login_flow
from usecases.registration_usecase import start_registration_flow

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/login", response_model=TokenResponse)
def login(
    request: LoginRequest,
    session: Session= Depends(get_session)
):  
    return start_login_flow(session=session, login_request=request)

@router.post("/register", response_model=TokenResponse)
def register_new_user(
    request: RegistrationRequest,
    session: Session= Depends(get_session)
):
   return start_registration_flow(
        session= session,
        useranme=request.useranme, 
        password=request.password,
        email=request.email,
        last_name=request.first_name, 
        first_name=request.last_name
    )

