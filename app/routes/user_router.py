from datetime import date
from fastapi import APIRouter, Depends, FastAPI, Security
from pydantic import BaseModel
from app.auth.hash_provider import get_password_hash, verify_password

from app.database.session import session_db
from ..database.database import Base, SessionLocal
from ..models.user_model import UserModel
from ..schemas.user_schema import ShowUser, User
from sqlalchemy.orm import Session
from ..database.database import engine
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
security = HTTPBearer()


# Dependency


router = APIRouter()


@router.post('/user' ,response_model=ShowUser , status_code=201)
async def create_user(request:User , db: Session = session_db() ):
    user = request
    user.password = get_password_hash(user.password)
    new_user = UserModel(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get('/user')
def get_all_user(db: Session = session_db()):
    user = db.query(UserModel).all()
    return user

@router.get('/user/{id}')
def get_user(id:int ,  db: Session = session_db()):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    return user






