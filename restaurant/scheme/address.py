from pydantic import BaseModel, Field, field_validator

from fastapi import HTTPException, status


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


class AddressForRead(BaseModel):
    id: int
    address: str
    customer_id: str

