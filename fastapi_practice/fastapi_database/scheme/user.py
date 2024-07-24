from pydantic import BaseModel, Field, field_validator

from datetime import datetime
import re

from fastapi import HTTPException, status


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
    username: str = Field(description='Length of your username should be between 1 and 16')
    password: str = Field(description='Password should be 8 character incloud: a-z, A-Z, 0-9 and one of !@#$%')
    phone_number: int = Field(description='Phone Number should start with 09 and length should be 11')

    @field_validator('username')
    @classmethod
    def username_validator(cls, username):
        if len(str(username)) == 0 or len(str(username)) > 16:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='length of username should be between 1 and 16'
            )

        return username

    @field_validator('password')
    @classmethod
    def password_validator(cls, password):
        if len(str(password)) != 8:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Password should be 8 character'
            )

        password_pattern = r'(?=.{1,}\d)(?=.{1,}[a-z])(?=.{1,}[A-Z])(?=.{1,}[!@#$%])'
        if bool(re.match(password_pattern, password)) is False:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Password should be 8 character contain: a-z, A-Z, 0-9 and one of !@#$%'
            )

        return password

    @field_validator('phone_number')
    @classmethod
    def phone_number_validator(cls, phone_number):
        phone_number_pattern = r'09[0-9]{9,9}'
        if bool(re.match(pattern=phone_number_pattern, string=phone_number)) is False:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Phone Number should start with 09 and length should be 11'
            )

    class Config:
        from_attributes = True

