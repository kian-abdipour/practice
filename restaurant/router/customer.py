from fastapi import APIRouter, HTTPException, status, Header, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from restaurant.database import get_session
from restaurant.scheme.customer import CustomerForLogin, CustomerForCreate, CustomerForRead, CustomerFilter
from restaurant.model.customer import Customer
from restaurant.model.cart import Cart
from restaurant.authentication import make_token, check_token, get_hash_password, verify_password
from restaurant.model.helper import Role

from sqlalchemy.orm import Session

from typing import Annotated

from datetime import timedelta

from fastapi_pagination import LimitOffsetPage, paginate, add_pagination
from fastapi_filter import FilterDepends


router = APIRouter(
    tags=['customer']
)
add_pagination(router)


@router.post('/customer-registrations')
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

    session.commit()

    return JSONResponse(content=body, headers=header)


@router.post('/customer-tokens')
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


@router.get('/customers', response_model=LimitOffsetPage[CustomerForRead])
def get(admin_token: Annotated[str, Header()],
        customer_filter: CustomerFilter = FilterDepends(CustomerFilter),
        session: Session = Depends(get_session)):
    token_payload = check_token(token=admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to see customers'
        )

    if customer_filter.id is not None:
        customer = Customer.search_by_id(session=session, customer_id=customer_filter.id)
        if customer is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Customer with this id not found'
            )

        customer_dict = customer.__dict__
        print(f'>>>>: {customer_dict}')
        customer_dict.pop('password')
        jsonable_customer = jsonable_encoder(customer)

        return JSONResponse(status_code=200, content=jsonable_customer)

    elif customer_filter.username is not None:
        customer = Customer.search_by_username(session=session, username=customer_filter.username)
        if customer is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Customer with this username not found'
            )

        customer_dict = customer.__dict__
        customer_dict.pop('password')
        jsonable_customer = jsonable_encoder(customer)

        return JSONResponse(status_code=200, content=jsonable_customer)

    elif customer_filter.phone_number is not None:
        customer = Customer.search_by_phone_number(session=session, phone_number=customer_filter.phone_number)
        if customer is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Customer with this phone number not found'
            )

        customer_dict = customer.__dict__
        customer_dict.pop('password')
        jsonable_customer = jsonable_encoder(customer)

        return JSONResponse(status_code=200, content=jsonable_customer)

    elif customer_filter.id is None and customer_filter.username is None and \
            customer_filter.phone_number is None:
        customers = Customer.show_all(session=session, customer_filter=customer_filter)

        return paginate(customers)

