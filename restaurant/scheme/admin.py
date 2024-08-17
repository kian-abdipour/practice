from pydantic import BaseModel, Field, field_validator

from fastapi import HTTPException, status

from re import match

from fastapi_filter.contrib.sqlalchemy import Filter

from restaurant.model import Admin

from typing import Optional, List

from datetime import datetime


class AdminForLogin(BaseModel):
    username: str = Field(description='Length of username should be at most 16 character')
    password: str = Field(description='Length of Password should be 8')

    @field_validator('username')
    @classmethod
    def validate_username(cls, username):
        if len(username) < 2 or len(username) > 20:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Length of username should be between at least 2 character and at most 16 character'
            )

        return username

    @field_validator('password')
    @classmethod
    def validate_password(cls, password):
        if len(password) != 8:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Length of password should be 8 character'
            )

        return password

    class Config:
        from_attributes = True


class AdminForAddition(BaseModel):
    first_name: str = Field(description='Length of first_name should be at most 40 character')
    last_name: str = Field(description='Length of last_name should be at most 40 character')
    username: str = Field(description='Length of username should be between at least 2 and at most 16 character')
    password: str = Field(
        description='Length of password should be 8 and password should contain: a-z, A-Z, 0-9, !@#$%'
    )

    @field_validator('first_name')
    @classmethod
    def validate_first_name(cls, first_name):
        if len(first_name) < 2 or len(first_name) > 16:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Length of first_name should be at most 40 character'
            )

        return first_name

    @field_validator('last_name')
    @classmethod
    def validate_last_name(cls, last_name):
        if len(last_name) < 2 or len(last_name) > 40:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Length of last_name should be at most 40 character'
            )

        return last_name

    @field_validator('username')
    @classmethod
    def validate_username(cls, username):
        if len(username) < 2 or len(username) > 20:
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
                detail='Length of password should be 8 character'
            )

        password_pattern = r'(?=.{1,}\d)(?=.{1,}[a-z])(?=.{1,}[A-Z])(?=.{1,}[!@#$%])'
        if bool(match(password_pattern, password)) is False:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Password should be 8 character contain: a-z, A-Z, 0-9 and one of !@#$%'
            )

        return password

    class Config:
        from_attributes = True


class AdminForRead(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    created_at: datetime

    class Config:
        from_attributes = True


class AdminFilter(Filter):
    class Constants(Filter.Constants):
        model = Admin

    id: int | None = None
    order_by: Optional[List[str]] = None

    @field_validator('order_by')
    @classmethod
    def validate_order_by(cls, order_by):
        print(order_by)
        admin_attributes = ['id', 'first_name', 'last_name', 'username', 'super_admin_id', 'created_at',
                            '-id', '-first_name', '-last_name', '-username', '-super_admin_id', '-created_at']
        for item in order_by:
            if item not in admin_attributes:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='order_by should be a valid attribute of Admin'
                )

        return order_by

