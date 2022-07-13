
from sqlalchemy import Column, Integer, String

from ..database.database import Base

class UserModel(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    age = Column(Integer)
    password = Column(String)

