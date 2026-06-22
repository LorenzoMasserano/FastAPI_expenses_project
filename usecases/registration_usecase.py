from fastapi import HTTPException, status
from pydantic import EmailStr
from sqlmodel import Session
from auth.schemas import TokenResponse
from config import settings

import auth.service as auth_service
import users.service as users_service
from utils.errors import raise_server_error

def start_registration_flow(
    session: Session,
    useranme: str,
    password: str,
    email: EmailStr, 
    first_name: str,
    last_name: str
):
    check_email_and_username(
        session=session,
        email=email,
        username=useranme
    )

    credential_id = auth_service.register(session=session, username=useranme, password=password).id
    if credential_id == None:
        raise_server_error()
    
    new_user_data = users_service.register_user_date(session=session, credential_id=credential_id, first_name=first_name, last_name=last_name, email=email)
    if new_user_data == None: 
        raise_server_error()

    tokens = auth_service.generate_jwt(credential_id=credential_id, secret_key=settings.SECRET_KEY) 
   
    return TokenResponse(
        token= tokens[auth_service.TokenType.ACCESS],
        refresh_token= tokens[auth_service.TokenType.REFRESH]
    )
    
def check_email_and_username(
    session: Session,
    email: EmailStr,
    username: str
):
    if users_service.is_email_already_used(session, email):
        raise_registration_error_field(
            error_type="invalid_email",
            error_message="the email is already in use",
            field_name_error="email",
            input_value=email
        )  

    if auth_service.is_username_already_used(session, username):
        raise_registration_error_field(
            error_type="INVALID_USERNAME",
            error_message="The username is already in use",
            field_name_error="username",
            input_value=username
        )

def raise_registration_error_field(
    error_type: str,
    error_message: str,
    field_name_error: str,
    input_value: str = "" 
):
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail=[
            {
                "type": f"business_logic.{error_type.lower()}", 
                "loc": ["body", field_name_error],
                "msg": error_message,
                "input": input_value
            }
        ]
    )
