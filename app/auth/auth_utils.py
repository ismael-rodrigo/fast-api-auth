from fastapi import Depends, HTTPException ,status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session
from app.database.session import session_db
from app.auth.token_provider import verify_access_token
from app.models.user_model import UserModel

oauth2_schema = OAuth2PasswordBearer(tokenUrl='auth/token')




def user_logged(token:str = Depends(oauth2_schema) , db: Session = session_db()):
    try:
        data = verify_access_token(token)
    except JWTError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED)

    user = db.query(UserModel).filter(UserModel.username == data).first()
    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED)    
    return user