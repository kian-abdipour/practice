from typing import Any

from pydantic import BaseModel, Field, field_validator

from fastapi import HTTPException, status
from pydantic.main import Model

from restaurant.model.helper import TypePay, State


class PaymentForRead(BaseModel):
    id: int
    state: str
    type: str
    amount: float
    customer_id: int

    class Config:
        from_attributes = True


class PaymentForCreate(BaseModel):
    state: str = Field(description='State should be Successful or Failed')
    type: str = Field(description='Pay Type should be one of Online or Cash or Transfer', default=TypePay.online)
    discount_code: str | None = Field(
        default=None,
        description='If you don\'t want discount code send it as empty string'
    )

    @field_validator('state')
    @classmethod
    def validate_state(cls, state):
        if state != State.successful and state != State.failed:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='State should be Successful or Failed'
            )

        return state

    @field_validator('type')
    @classmethod
    def validate_type(cls, type_):
        if type_ != TypePay.online and type_ != TypePay.cash and type_ != TypePay.transfer:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Pay Type should be one of Online or Cash or Transfer'
            )

        return type_

    class Config:
        from_attributes = True

