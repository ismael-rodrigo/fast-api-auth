from fastapi import APIRouter, Depends, HTTPException ,status
from jose import JWTError
from core.auth.auth_utils import user_logged
from core.auth.hash_provider import verify_password
from core.auth.token_provider import create_access_token ,refresh_token
from core.database.session import get_db
from core.models.user_model import UserModel
from core.schemas.auth_login_schema import LoginToken
from sqlalchemy.orm import Session
from core.schemas.token_schemas import RefreshToken
from core.schemas.user_schema import ShowUser, User


router = APIRouter()

@router.post('/token')
def get_token(credentials:LoginToken ,db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.username == credentials.username).first()
    if not user:
        raise HTTPException(status.HTTP_400_BAD_REQUEST , detail='password or username invalid')

    if not verify_password(credentials.password ,user.password ):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED ,detail='password or username invalid')
    
    token = create_access_token({'sub':str(user.id)})
    return token



@router.get('/verify' )
def verify(user:User = Depends(user_logged)):
    return HTTPException(status.HTTP_200_OK ,detail='token is valid')





@router.post('/refresh')
def refresh(refresh :RefreshToken):
    try:
        access = refresh_token(refresh.refresh)
    except JWTError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED , detail='invalid refresh token')

    return access

