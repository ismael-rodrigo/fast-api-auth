
from sqlalchemy import Column, Integer, String

from .database import Base

class UserModel(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    date = Column(String)
