from pydantic import BaseModel, Field, field_validator

from fastapi import HTTPException, status

from restaurant.model.helper import State, DeliveryType

from datetime import datetime


class OrderForCreate(BaseModel):
    delivery_type: str = Field(
        description='Delivery type should be one of Bike delivery or In restaurant or Outside'
    )
    desk_number: int = Field(description='Desk number should be integer')
    description: str | None = Field(description='If you don\'t want to add any description sent an empty string')
    payment_id: int
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

    @field_validator('description')
    @classmethod
    def validate_description(cls, description):
        if description == '':
            return None

        return description

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

