from pydantic import BaseModel, Field, field_validator

from fastapi import HTTPException, status

from datetime import datetime

from fastapi_filter.contrib.sqlalchemy import Filter
from pydantic_core.core_schema import ValidationInfo

from restaurant.model import Item

from typing import List, Optional


class ItemForCreate(BaseModel):
    name: str = Field(description='An item name should be at least 40 character')
    country: str = Field(description='A country name should be at least 30 character')
    price: float = Field()
    stock: int = Field(default=0)
    description: str | None = Field(description='If you don\'t want to add any description sent an empty string')

    @field_validator('name')
    @classmethod
    def validate_name(cls, name):
        if len(name) > 40:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='An item name should be at least 40 character'
            )

        return name

    @field_validator('country')
    @classmethod
    def validate(cls, country):
        if len(country) > 30:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='A country name should be at least 30 character'
            )

        return country

    @field_validator('description')
    @classmethod
    def validate_description(cls, description):
        if description == '':
            return None

        return description

    class Config:
        from_attributes = True


class ItemForRead(BaseModel):
    id: int
    name: str
    country: str
    price: float
    stock: int
    description: str | None
    created_at: datetime

    class Config:
        from_attributes = True


class ItemOutOfStock(ItemForRead):
    quantity: int

    class Config:
        from_attributes = True



class ItemFilter(Filter):
    class Constants(Filter.Constants):
        model = Item

    id: int | None = None
    name: str | None = None
    order_by: Optional[List[str]] = None

    @field_validator('order_by')
    @classmethod
    def validate_order_by(cls, order_by):
        item_attributes = ['id', 'name', 'country', 'price', 'stock',
                           '-id', '-name', '-country', '-price', '-stock']
        for item in order_by:
            if item not in item_attributes:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='order by should be a valid attribute of item'
                )

        return order_by

    @field_validator('name')
    @classmethod
    def validate_name(cls, name):
        if len(name) > 40:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='An item name should be at least 40 character'
            )

        return name


class ItemInCartFilter(Filter):
    class Constants(Filter.Constants):
        model = Item

    order_by: Optional[List[str]] = None

    @field_validator('order_by')
    @classmethod
    def validate_order_by(cls, order_by):
        item_attributes = ['id', 'name', 'country', 'price', 'stock',
                           '-id', '-name', '-country', '-price', '-stock']
        for item in order_by:
            if item not in item_attributes:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='order by should be a valid attribute of item'
                )

        return order_by


class ItemInCategoryFilter(ItemInCartFilter):
    class Constants(Filter.Constants):
        model = Item

    category_id: int


