from pydantic import BaseModel, Field, field_validator

from fastapi import HTTPException, status


class CartItemForCreate(BaseModel):
    item_id: int
    cart_id: int
    quantity: int = Field(default=1)

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

