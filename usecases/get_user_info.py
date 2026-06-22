from sqlmodel import Session
from users.schemas import UserInfo
import users.service as users_service
import auth.service as auth_service
from config import settings
from utils.errors import raise_server_error

def get_user_info(session: Session, access_token: str) -> UserInfo:

    credential_id = auth_service.verify_token_validity(token=access_token, secret_key=settings.SECRET_KEY)
    user_data = users_service.get_user_data(session=session, credential_id= credential_id)
   
    if user_data == None:
        raise_server_error() 

    return UserInfo(
        first_name= user_data.first_name,
        last_name= user_data.last_name,
        email= user_data.email
    )
