from pydantic import BaseModel


class UserForAuthentication(BaseModel):
    username: str
    password: str


class User(UserForAuthentication):
    is_valid: bool | None = None

