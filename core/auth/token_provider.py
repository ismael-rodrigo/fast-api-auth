from datetime import datetime, timedelta
from jose import jwt
from core.settings import settings

SECRET_KEY = settings.SECRET_KEY
REFRESH_SECRET_KEY = settings.REFRESH_SECRET_KEY

ALGORITHM = settings.ALGORITHM
ACCESS_EXPIRES_IN_MIN = settings.ACCESS_EXPIRES_IN_MIN
REFRESH_EXPIRES_IN_MIN = settings.REFRESH_EXPIRES_IN_MIN


def create_access_token(_data:dict):
    data_access ,data_refresh = _data.copy() , _data.copy() 

    expiration_access = datetime.utcnow() + timedelta(minutes=ACCESS_EXPIRES_IN_MIN)
    expiration_refresh = datetime.utcnow() + timedelta(minutes=REFRESH_EXPIRES_IN_MIN)

    data_access.update({'exp':expiration_access})
    data_refresh.update({'exp':expiration_refresh})

    access_token = jwt.encode(data_access ,key=SECRET_KEY , algorithm=ALGORITHM )

    refresh_token = jwt.encode(data_refresh ,key=REFRESH_SECRET_KEY , algorithm=ALGORITHM )

    return {
        'access' :access_token,
        'refresh':refresh_token
    }



def verify_access_token(token:str):
    data = jwt.decode(token ,key=SECRET_KEY ,algorithms=[ALGORITHM])
    return data.get('sub')




def refresh_token(refresh_token:str):

    data = jwt.decode(token=refresh_token ,key=REFRESH_SECRET_KEY ,algorithms=[ALGORITHM])
    expiration_access = datetime.utcnow() + timedelta(minutes=ACCESS_EXPIRES_IN_MIN)
    data.update({'exp':expiration_access})
    new_access_token = jwt.encode(data , SECRET_KEY ,algorithm=ALGORITHM)

    return {"access": new_access_token}