from pydantic import BaseModel

from datetime import datetime


class User(BaseModel):
    id: int
    username: str
    password: str

    class Config:
        from_attributes = True


class UserForRead(BaseModel):
    id: int
    username: str
    created_at: datetime

    class Config:
        from_attributes = True


class UserForLogin(BaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True

