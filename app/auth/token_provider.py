from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = '0f1c88f36f9edd1ed0f56e4d8d1674e17a1bc6fab6803a7125789f7b4cf7dc05'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 20


def create_access_token(_data:dict):
    data = _data.copy()
    expiration = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)
    data.update({'exp':expiration})
    token = jwt.encode(data ,key=SECRET_KEY , algorithm=ALGORITHM )
    return token

def verify_access_token(token:str):
    data = jwt.decode(token ,key=SECRET_KEY ,algorithms=[ALGORITHM])
    return data.get('sub')

