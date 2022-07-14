from typing import List
from pydantic import BaseModel
from decouple import config

#
DEBUG = config('DEBUG',cast=bool)


#---CORS CONFIGS---
CORS_ORIGINS_DEBUG_TRUE = [
        '*',
    ]

CORS_ORIGINS_DEBUG_FALSE =  [
        "http://site-frontend.com",
        "https://site-frontend.com",
    ]


#---JWT CONFIGS---
ACCESS_EXPIRES_IN_MIN  = 10
REFRESH_EXPIRES_IN_MIN = 50








class Settings(BaseModel):

    CORS_ORIGINS: List[str] = CORS_ORIGINS_DEBUG_FALSE if not DEBUG else CORS_ORIGINS_DEBUG_TRUE

    SECRET_KEY: str = config('SECRET_KEY')
    REFRESH_SECRET_KEY: str = config('REFRESH_SECRET_KEY')
    ALGORITHM: str = config('ALGORITHM')
    ACCESS_EXPIRES_IN_MIN: int = ACCESS_EXPIRES_IN_MIN
    REFRESH_EXPIRES_IN_MIN: int = REFRESH_EXPIRES_IN_MIN

    DATABASE_URL: str = config('DATABASE_URL_PROD') if not DEBUG else config('DATABASE_URL_DEV')


settings = Settings()



