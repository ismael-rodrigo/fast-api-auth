from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    name:str
    age:int
    date:str
    class Config:
        orm_mode = True

class ShowUser(BaseModel):
    name:str
    class Config:
        orm_mode = True