from pydantic import BaseModel

from datetime import datetime


class User(BaseModel):
    id: int
    username: str
    password: str

    class Config:
        from_attributes = True


class UserForRead(BaseModel):
    created_at: datetime
    id: int
    username: str

    class Config:
        from_attributes = True


class UserForLogin(BaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True

