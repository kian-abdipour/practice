import hashlib

from fastapi import APIRouter, HTTPException, status, Header, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from restaurant.database import get_session
from restaurant.scheme.customer import CustomerForLogin
from restaurant.model.customer import Customer
from restaurant.model.cart import Cart
from restaurant.authentication import make_token, check_token, get_hash_password, verify_password

from sqlalchemy.orm import Session

from typing import Any

from datetime import timedelta


router = APIRouter(
    prefix='/customer',
    tags=['customer']
)

role = 'customer'


@router.post('/tokens')
def signup(session: Session = Depends(get_session), customer: CustomerForLogin = Any) -> Any:
    if Customer.search_by_username(session, customer) is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='This username already exist choose another one'
        )

    hashed_password = get_hash_password(password=customer.password)
    added_customer = Customer.add(
        session=session, username=customer.username,
        password=hashed_password, phone_number=customer.phone_number
    )
    Cart.add(session=session, customer_id=added_customer.id)

    customer_dict = added_customer.__dict__
    customer_dict.pop('password')
    body = jsonable_encoder(customer_dict)

    token = make_token(
        id_=added_customer.id,
        role=role,
        username=added_customer.username,
        expire_delta=timedelta(seconds=20)
    )
    header = {'token': token}

    return JSONResponse(content=body, headers=header)


@router.post('/tokens')
def login(session: Session = Depends(get_session), customer: CustomerForLogin = Any) -> Any:
    customer_in_database = Customer.search_by_username(
        session=session,
        username=customer.username,
    )

    if customer_in_database is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Username not found'
        )

    if verify_password(customer.password, customer_in_database.password) is False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Password is not correct'
        )

    customer_dict = customer_in_database.__dict__
    customer_dict.pop('password')
    body = jsonable_encoder(customer_dict)

    token = make_token(
        id_=customer_in_database.id,
        role=role,
        username=customer_in_database.username,
        expire_delta=timedelta(seconds=20)
    )
    header = {'token': token}

    return JSONResponse(content=body, headers=header)

