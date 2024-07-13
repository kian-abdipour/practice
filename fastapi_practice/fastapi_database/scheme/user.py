from pydantic import BaseModel

from datetime import datetime


class User(BaseModel):
    id: int
    username: str
    password: str

    class Config:
        orm_mode = True


class UserForRead(BaseModel):
    id: int
    username: str
    created_at: datetime

    class Config:
        orm_mode = True


class UserForLogin(BaseModel):
    username: str
    password: str

