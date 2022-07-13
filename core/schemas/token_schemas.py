

from pydantic import BaseModel


class RefreshToken(BaseModel):
    refresh:str