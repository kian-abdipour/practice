from pydantic import BaseModel, Field, field_validator

from fastapi import HTTPException, status

from restaurant.model.helper import State, DeliveryType, TypePay
from restaurant.model import Order

from datetime import datetime

from fastapi_filter.contrib.sqlalchemy import Filter

from typing import Optional, List


class OrderForCreate(BaseModel):
    delivery_type: str = Field(
        description='Delivery type should be one of Bike delivery or In restaurant or Outside'
    )
    desk_number: int | None = Field(description='Desk number should be integer')
    description: str | None
    payment_type: str
    discount_code: str | None
    address_id: int

    @field_validator('delivery_type')
    @classmethod
    def validate_delivery_type(cls, delivery_type):
        if delivery_type != DeliveryType.eat_in_restaurant and \
                delivery_type != DeliveryType.eat_out and \
                delivery_type != DeliveryType.bike_delivery:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Delivery type should be one of'
                       f' {DeliveryType.bike_delivery} or {DeliveryType.eat_out} or {DeliveryType.eat_in_restaurant}'
            )

        return delivery_type

    @field_validator('payment_type')
    @classmethod
    def validate_type(cls, payment_type):
        if payment_type != TypePay.online and payment_type != TypePay.cash and payment_type != TypePay.transfer:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Pay Type should be one of Online or Cash or Transfer'
            )

        return payment_type

    @field_validator('desk_number')
    @classmethod
    def validate_desk_number(cls, desk_number, delivery_type):
        delivery_type = delivery_type.data['delivery_type']
        if delivery_type == DeliveryType.eat_out or delivery_type == DeliveryType.bike_delivery:
            return None

        else:
            return desk_number

    class Config:
        from_attributes = True


class OrderForRead(BaseModel):
    id: int
    state: str
    delivery_type: str
    desk_number: int | None
    description: str | None
    payment_id: int
    address_id: int
    customer_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class OrderFilter(Filter):
    class Constants(Filter.Constants):
        model = Order

    id: int | None = None
    state: str | None = None
    order_by: Optional[List[str]] = None

    @field_validator('order_by')
    @classmethod
    def validate_order_by(cls, order_by):
        item_attributes = ['id', 'state', 'delivery_type', 'desk_number', 'customer_id',
                           '-id', '-state', '-delivery_type', '-desk_number', '-customer_id']
        for item in order_by:
            if item not in item_attributes:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='order by should be a valid attribute of order'
                )

        return order_by

    @field_validator('state')
    @classmethod
    def validate_state(cls, state):
        if state != State.confirm_and_finish and state != State.waiting_to_confirmation:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'An state should be {State.confirm_and_finish} or {State.waiting_to_confirmation}'
            )

        return state



