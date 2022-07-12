from fastapi import Depends
from app.database.database import SessionLocal


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def session_db():
    return Depends(get_db)