from fastapi import APIRouter, HTTPException, status, Header, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from restaurant.database import get_session
from restaurant.scheme.customer import CustomerForLogin, CustomerForCreate, CustomerForRead
from restaurant.model.customer import Customer
from restaurant.model.cart import Cart
from restaurant.authentication import make_token, check_token, get_hash_password, verify_password
from restaurant.model.helper import Role

from sqlalchemy.orm import Session

from typing import Any, List

from datetime import timedelta


router = APIRouter(
    prefix='/customers',
    tags=['customer']
)


@router.post('/signup/tokens')
def signup(customer: CustomerForCreate, session: Session = Depends(get_session)):
    if Customer.search_by_username(session=session, username=customer.username) is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='This username already exist choose another one'
        )

    if Customer.search_by_phone_number(session=session, phone_number=customer.phone_number) is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='This phone number already have an account choose another one or login'
        )

    hashed_password = get_hash_password(password=customer.password)
    added_customer = Customer.add(
        session=session, username=customer.username,
        password=hashed_password, phone_number=customer.phone_number
    )
    Cart.add(session=session, customer_id=added_customer.id)

    customer_dict = added_customer.__convert_to_dict__()
    customer_dict.pop('password')
    body = jsonable_encoder(customer_dict)

    token = make_token(
        id_=added_customer.id,
        role=Role.customer,
        username=added_customer.username,
        expire_delta=timedelta(hours=1)
    )
    header = {'token': token}

    return JSONResponse(content=body, headers=header)


@router.post('/login/tokens')
def login(customer: CustomerForLogin, session: Session = Depends(get_session)):
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
    print(f'>>>>: {customer_dict}')
    customer_dict.pop('password')
    body = jsonable_encoder(customer_dict)

    token = make_token(
        id_=customer_in_database.id,
        role=Role.customer,
        username=customer_in_database.username,
        expire_delta=timedelta(hours=1)
    )
    header = {'token': token}

    return JSONResponse(content=body, headers=header)


@router.get('', response_model=List[CustomerForRead])
def show_all(admin_token: str, session: Session = Depends(get_session)):
    token_payload = check_token(token=admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to see customers'
        )

    customers = Customer.show_all(session=session)

    return customers


@router.get('/{username}', response_model=CustomerForRead)
def show_specific(admin_token: str, username: str, session: Session = Depends(get_session)):
    token_payload = check_token(token=admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to see discounts'
        )

    customer = Customer.search_by_username(session=session, username=username)
    if customer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='An customer with this username not found'
        )

    return customer

