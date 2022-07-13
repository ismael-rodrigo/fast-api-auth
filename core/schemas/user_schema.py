from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    username:str
    age:int
    password:str
    class Config:
        orm_mode = True

class ShowUser(BaseModel):
    username:str
    age:int
    class Config:
        orm_mode = True