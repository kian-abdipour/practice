from pydantic import BaseModel, Field, field_validator

from fastapi import HTTPException, status

from datetime import datetime

from fastapi_filter.contrib.sqlalchemy import Filter

from restaurant.model import Category

from typing import Optional, List


class CategoryForCreate(BaseModel):
    name: str = Field(description='Category name should be at least 40 character')

    @field_validator('name')
    @classmethod
    def validate_name(cls, name):
        if len(name) > 40:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Category name should be at least 40 character'
            )

        return name

    class Config:
        from_attributes = True


class CategoryForRead(BaseModel):
    id: int = Field(description='Id should be integer')
    name: str = Field(description='Category name should be at least 40 character')
    created_at: datetime

    @field_validator('name')
    @classmethod
    def validate_name(cls, name):
        if len(name) > 40:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Category name should be at least 40 character'
            )

        return name

    class Config:
        from_attributes = True


class CategoryFilter(Filter):
    class Constants(Filter.Constants):
        model = Category

    id: int | None = None
    name: str | None = None
    order_by: Optional[List[str]] = None

    @field_validator('order_by')
    @classmethod
    def validate_order_by(cls, order_by):
        print(order_by)
        admin_attributes = ['id', 'name',
                            '-id', '-name',]
        for item in order_by:
            if item not in admin_attributes:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='order_by should be a valid attribute of Admin'
                )

        return order_by

