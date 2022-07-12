from venv import create
from fastapi import APIRouter, Depends, HTTPException ,status
from app.auth.auth_utils import user_logged
from app.auth.hash_provider import verify_password
from app.auth.token_provider import create_access_token
from app.database.session import session_db
from app.models.user_model import UserModel

from app.schemas.auth_login_schema import LoginToken
from sqlalchemy.orm import Session

from app.schemas.user_schema import ShowUser, User


router = APIRouter()

@router.post('/token')
def get_token(credentials:LoginToken ,db: Session = session_db() ):
    user = db.query(UserModel).filter(UserModel.username == credentials.username).first()
    if not user:
        raise HTTPException(status.HTTP_400_BAD_REQUEST , detail='password or username invalid')

    if not verify_password(credentials.password ,user.password ):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED ,detail='password or username invalid')
    
    token = create_access_token({'sub':user.username})
    return token



@router.get('/verify' ,response_model=ShowUser)
def me(user:User = Depends(user_logged) ):
    return user

