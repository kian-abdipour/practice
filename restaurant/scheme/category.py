from pydantic import BaseModel, Field, field_validator

from fastapi import HTTPException, status

from datetime import datetime


class CategoryForCreate(BaseModel):
    name: str = Field(description='Category name should be at least 40 character')

    @field_validator('name')
    @classmethod
    def validate_name(cls, name):
        if len(name) > 40:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Category name should be at least 40 character'
            )

        return name

    class Config:
        from_attributes = True


class CategoryForRead(BaseModel):
    id: int = Field(description='Id should be integer')
    name: str = Field(description='Category name should be at least 40 character')
    created_at: datetime

    @field_validator('name')
    @classmethod
    def validate_name(cls, name):
        if len(name) > 40:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Category name should be at least 40 character'
            )

        return name

    class Config:
        from_attributes = True

