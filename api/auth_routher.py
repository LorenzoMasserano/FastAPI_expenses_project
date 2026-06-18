from fastapi import APIRouter, Depends
from sqlmodel import Session

from auth.schemas import LoginRequest, TokenResponse
from database import get_session
from usecases.login_usecase import start_login_flow

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/login", response_model=TokenResponse)
def login(
    login_request: LoginRequest,
    session: Session= Depends(get_session)
):  
    return start_login_flow(session=session, login_request=login_request)

