from fastapi import APIRouter, Depends
from sqlmodel import Session

from usecases.get_user_info import get_user_info
from database import get_session
from users.schemas import UserInfo
from auth.service import oauth2_scheme

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.get("/", response_model=UserInfo)
def request_user_info(
    session: Session= Depends(get_session),
    token: str = Depends(oauth2_scheme)
):  
    return get_user_info(session=session, access_token= token)
