from pydantic import BaseModel


class LoginToken(BaseModel):
    username:str
    password:str

