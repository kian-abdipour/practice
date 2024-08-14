from pydantic import BaseModel, Field, field_validator

from fastapi import HTTPException, status

from fastapi_filter.contrib.sqlalchemy import Filter

from typing import Optional, List

from restaurant.model import Address


class AddressForAddition(BaseModel):
    address: str = Field(description='Length of address should not be more than 150 character')

    @field_validator('address')
    @classmethod
    def validate_address(cls, address):
        if len(address) > 150:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Password is to long it should be at most 150 character'
            )

        return address

    class Config:
        from_attributes = True


class AddressForRead(BaseModel):
    id: int
    address: str
    customer_id: int

    class Config:
        from_attributes = True


class AddressFilter(Filter):
    class Constants(Filter.Constants):
        model = Address

    address_id: int | None = None
    order_by: Optional[List[str]] = None

    @field_validator('order_by')
    @classmethod
    def validate_order_by(cls, order_by):
        list_address_attribute = ['id', 'address', 'customer_id', '-id', '-address', '-customer_id']
        for item in order_by:
            if item not in list_address_attribute:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='order_by should be a valid attribute of Address'
                )

        return order_by

