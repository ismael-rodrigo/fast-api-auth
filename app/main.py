from fastapi import Depends, FastAPI
from .database import Base, SessionLocal
from .models import UserModel
from .schemas import ShowUser, User
from sqlalchemy.orm import Session
from .database import engine


Base.metadata.create_all(bind=engine)


app = FastAPI()


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()






@app.post('/user' ,response_model=ShowUser)
def create_user(request:User , db: Session = Depends(get_db)):
    new_user = UserModel( name=request.name ,age= request.age)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@app.get('/user')
def get_all_user(db: Session = Depends(get_db)):
    user = db.query(UserModel).all()
    return user
