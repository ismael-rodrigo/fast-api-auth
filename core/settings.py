from pydantic import BaseModel
from decouple import config


DEBUG = config('DEBUG',cast=bool)


class Settings(BaseModel):
    SECRET_KEY: str = config('SECRET_KEY')
    REFRESH_SECRET_KEY: str = config('REFRESH_SECRET_KEY')
    ALGORITHM: str = config('ALGORITHM')
    ACCESS_EXPIRES_IN_MIN: int = 10
    REFRESH_EXPIRES_IN_MIN: int = 30


    DATABASE_URL: str = config('DATABASE_URL') if not DEBUG else 'sqlite:///./database.db'


settings = Settings()

