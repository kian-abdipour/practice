from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    password: str

    class Config:
        orm_mode = True


class UserForRead(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


class UserForLogin(BaseModel):
    username: str
    password: str

