from pydantic import BaseModel

class UserInfo(BaseModel):
    first_name:str 
    last_name:str 
    email:str 
