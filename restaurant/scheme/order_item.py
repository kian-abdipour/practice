from pydantic import BaseModel, Field, field_validator

from fastapi import HTTPException, status


class OrderItemForCreate(BaseModel):
    quantity: int
    unit_amount: float
    order_id: int
    item_id: int

    class Config:
        from_attributes = True


class OrderItemForRead(BaseModel):
    id: int
    quantity: int
    unit_amount: float
    total_amount: float
    order_id: int
    item_id: int

    class Config:
        from_attributes = True

