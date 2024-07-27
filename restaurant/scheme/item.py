from pydantic import BaseModel, Field, field_validator

from fastapi import HTTPException, status


class ItemForCreate(BaseModel):
    name: str = Field(description='An item name should be at least 40 character')
    country: str = Field(description='A country name should be at least 30 character')
    price: float = Field()
    stock: int = Field(default=0)
    description: str = Field(description='If you don\'t want to add any description sent an empty string')

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
    price: int
    stock: int
    description: str

    class Config:
        from_attributes = True


