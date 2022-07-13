from fastapi import Depends, HTTPException ,status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session
from core.database.session import get_db
from core.auth.token_provider import verify_access_token
from core.models.user_model import UserModel

oauth2_schema = OAuth2PasswordBearer(tokenUrl='auth/token')


def user_logged(token:str = Depends(oauth2_schema) , db: Session = Depends(get_db)):
    try:
        data = verify_access_token(token)
    except JWTError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED , detail='token invalid')

    user = db.query(UserModel).filter(UserModel.id == data).first()
    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED , detail='token invalid')    
    return user