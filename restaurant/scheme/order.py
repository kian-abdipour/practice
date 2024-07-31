from pydantic import BaseModel, Field, field_validator

from fastapi import HTTPException, status

from restaurant.model.helper import State, DeliveryType


class OrderForCreate(BaseModel):
#    state: str = Field(
#        description='Order state should be one of: Waiting to confirmation or Successfully confirm and finish'
#    )
    delivery_type: str = Field(
        description='Delivery type should be one of "Bike delivery" or "In restaurant" or "Outside"'

    )
    desk_number: int = Field(description='Desk number should be integer')
    description: str = Field(description='If you don\'t want to add any description sent an empty string')
    address_id: int = Field()

    @field_validator('delivery_type')
    @classmethod
    def validate_delivery_type(cls, delivery_type):
        if delivery_type != DeliveryType.eat_in_restaurant and \
                delivery_type != DeliveryType.eat_in_restaurant and \
                delivery_type != DeliveryType.bike_delivery:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Delivery type should be one of "Bike delivery" or "In restaurant" or "Outside"'
            )

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
    desk_number: int
    description: str
    address_id: int
    customer_id: int

    class Config:
        from_attributes = True

