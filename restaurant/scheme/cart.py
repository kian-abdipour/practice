from pydantic import BaseModel, Field, field_validator

from fastapi import HTTPException, status

from fastapi_filter.contrib.sqlalchemy import Filter

from restaurant.model import CartItem

from typing import Optional, List


class CartItemForCreate(BaseModel):
    item_id: int
    quantity: int = Field(description='Quantity should be integer -1 or 1')

    @field_validator('quantity')
    @classmethod
    def validate_quantity(cls, quantity):
        if quantity != -1 and quantity != 1:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Quantity should be integer -1 or 1'
            )

        return quantity

    class Config:
        from_attributes = True


class CartItemForRead(BaseModel):
    id: int
    item_id: int
    cart_id: int
    quantity: int
    unit_amount: float
    total_amount: float

    class Config:
        from_attributes = True


class CartForRead(BaseModel):
    id: int
    customer_id: int
    total_quantity: int
    total_amount: int

    class Config:
        from_attributes = True


class CartItemFilter(Filter):
    class Constants(Filter.Constants):
        model = CartItem

    order_by: Optional[List[str]] = None

    @field_validator('order_by')
    @classmethod
    def validate_order_by(cls, order_by):
        item_attributes = ['id', 'quantity', 'unit_amount', 'total_amount',
                           '-id', '-quantity', '-unit_amount', '-total_amount',]
        for item in order_by:
            if item not in item_attributes:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='order by should be a valid attribute of cart_item'
                )

        return order_by

