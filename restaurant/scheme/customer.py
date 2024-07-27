from re import match

from pydantic import BaseModel, Field, field_validator

from fastapi import HTTPException, status


class CustomerForLogin(BaseModel):
    username: str = Field(description='Length of username should be at least 2 and at most 20')
    password: str = Field(
        description='Length of password should be 8 and password should contain: a-z, A-Z, 0-9, !@#$%'
    )

    @field_validator('username')
    @classmethod
    def validate_username(cls, username):
        if 2 > len(username) > 20:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Length of username should be at least 2 and at most 20'

            )

        return username

    @field_validator('password')
    @classmethod
    def validate_password(cls, password):
        if len(password) != 8:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Length of password should be 8'
            )

        password_pattern = r'(?=.{1,}\d)(?=.{1,}[a-z])(?=.{1,}[A-Z])(?=.{1,}[!@#$%])'
        if bool(match(password_pattern, password)) is False:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail='Password should be 8 character contain: a-z, A-Z, 0-9 and one of !@#$%')

        return password

    class Config:
        from_attributes = True

    class Config:
        from_attributes = True

