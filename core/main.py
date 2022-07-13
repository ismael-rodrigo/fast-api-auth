
from core.routes import user_route , auth_route



from fastapi import FastAPI


app = FastAPI()


app.include_router(user_route.router ,prefix='')
app.include_router(auth_route.router  ,prefix='/auth')