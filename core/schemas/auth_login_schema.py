from pydantic import BaseModel


class LoginToken(BaseModel):
    username:str
    password:str

    class Config:
        orm_mode = True
