from pydantic import BaseModel, field_validator, Field

from fastapi import HTTPException, status


class SuperAdminForLogin(BaseModel):
    username: str = Field(description='Length of Username should be between at least 2 and at most 16 character')
    password: str = Field(description='Length of password should be 8')

    @field_validator('username')
    @classmethod
    def validate_username(cls, username):
        if 2 > len(username) > 16:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Length of Username should be between at least 2 and at most 16 character'
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


class SuperAdminForCreate(BaseModel):
    first_name: str = Field(description='Length of first_name should be at most 40 character')
    last_name: str = Field(description='Length of last_name should be at most 40 character')
    username: str = Field(description='Length of username should be between at least 2 and at most 16 character')
    password: str = Field(
        description='Length of password should be 8 and password should contain: a-z, A-Z, 0-9, !@#$%'
    )

    @field_validator('first_name')
    @classmethod
    def validate_first_name(cls, first_name):
        if 2 > len(first_name) > 16:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Length of first_name should be at most 40 character'
            )

        return first_name

    @field_validator('last_name')
    @classmethod
    def validate_first_name(cls, last_name):
        if 2 > len(last_name) > 16:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Length of last_name should be at most 40 character'
            )

        return last_name

    @field_validator('username')
    @classmethod
    def validate_username(cls, username):
        if 2 > len(username) > 16:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Length of Username should be between at least 2 and at most 16 character'
            )

        return username

    @field_validator('password')
    @classmethod
    def validate_first_name(cls, password):
        if 2 > len(password) > 16:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Length of password should be at most 16 character'
            )

        return password


class SuperAdminForRead(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str

