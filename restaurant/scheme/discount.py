from pydantic import BaseModel, Field, field_validator

from datetime import date, datetime

from re import match

from fastapi import HTTPException, status


class DiscountForRead(BaseModel):
    id: int
    start_date: date
    expire_date: date
    title: str
    percent: float
    code: str
    description: str | None
    usage_limitation: str | None
    disposable: bool
    created_at: datetime


class DiscountForCreate(BaseModel):
    start_date: str = Field(description='Start date should be like 2024-07-12')
    expire_date: str = Field(description='End date should be like 2024-07-12')
    title: str = Field(description='Length of title should be at least 40 character')
    percent: float = Field(description='Percent should be between 0.1 to 0.99')
    description: str | None
    usage_limitation: str | None = Field(description='Usage limitation should be positive integer')
    disposable: bool = Field()

    @field_validator('start_date')
    @classmethod
    def validate_start_date(cls, start_date):
        pattern = '[0-9]{4,4}-[0-9]{2,2}-[0-9]{2,2}'
        if bool(match(pattern=pattern, string=start_date)) is False:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Start date should be like 2024-7-12'
            )

        list_start_date = start_date.split('-')
        start_date = date(year=int(list_start_date[0]),
                          month=int(list_start_date[1]),
                          day=int(list_start_date[2]))

        return start_date

    @field_validator('expire_date')
    @classmethod
    def validate_start_date(cls, expire_date):
        pattern = '[0-9]{4,4}-[0-9]{2,2}-[0-9]{2,2}'
        if bool(match(pattern=pattern, string=expire_date)) is False:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Expire date should be like 2024-07-12'
            )

        list_expire_date = expire_date.split('-')
        expire_date = date(year=int(list_expire_date[0]),
                           month=int(list_expire_date[1]),
                           day=int(list_expire_date[2]))

        return expire_date

    @field_validator('title')
    @classmethod
    def validate_title(cls, title):
        if len(title) > 40:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Length of title should be at least 40 character'
            )

        return title


    @field_validator('percent')
    @classmethod
    def validate_percent(cls, percent):
        if 0.1 > percent > 0.99:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Percent should be between 0.1 to 0.99'
            )

        return percent

    @field_validator('usage_limitation')
    @classmethod
    def validate_usage_limitation(cls, usage_limitation):
        if usage_limitation is not None:
            if usage_limitation < 0:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='Usage limitation should be positive integer'
                )

        return usage_limitation

    @field_validator('disposable')
    @classmethod
    def validate_disposable(cls, disposable):
        if disposable is False:
            return False

        elif disposable is True:
            return True

        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Disposable should be bool like true or false'
            )

