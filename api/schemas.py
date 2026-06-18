from pydantic import BaseModel, EmailStr, field_validator
import re

class RegistrationRequest(BaseModel):
    useranme: str
    password: str
    email: EmailStr

    first_name: str
    last_name: str

    @field_validator('password')
    @classmethod
    def validate_password_strength(cls, value: str) -> str:
        if len(value) < 8:
            raise ValueError('The password must have at least 8 characters.')
            
        if not re.search(r"[A-Z]", value):
            raise ValueError('The password must have at least 1 Upperace character.')
            
        if not re.search(r"[a-z]", value):
            raise ValueError('The password must have at least 1 Lowercase character.')
            
        if not re.search(r"\d", value):
            raise ValueError('The password must contain at least 1 number.')
            
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError('The password must contain at least 1 special char.')
            
        return value

    @field_validator('first_name')
    @classmethod
    def validate_first_name_strength(cls, value: str) -> str:
        if len(value) < 1:
            raise ValueError('First name is empty.')
            
        return value   


    @field_validator('last_name')
    @classmethod
    def validate_last_name_strength(cls, value: str) -> str:
        if len(value) < 1:
            raise ValueError('Last name is empty.')
            
        return value   
