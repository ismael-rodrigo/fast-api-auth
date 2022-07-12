
from app.routes import user_router , auth_route



from fastapi import FastAPI


app = FastAPI()


app.include_router(user_router.router ,prefix='')
app.include_router(auth_route.router  ,prefix='/auth')