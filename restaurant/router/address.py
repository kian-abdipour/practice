from fastapi import APIRouter, Depends, HTTPException, status

from restaurant.database import get_session
from restaurant.authentication import check_token
from restaurant.model import Address, Customer
from restaurant.scheme.address import AddressForAddition, AddressForRead

from sqlalchemy.orm import Session

from typing import Any


router = APIRouter(
    prefix='/addresses',
    tags=['address']
)

role = 'customer'


@router.post('', response_model=AddressForRead)
def addition(customer_token: str, address: AddressForAddition, session: Session = Depends(get_session)):
    token_payload = check_token(token=customer_token)
    token_role = token_payload['role']
    if token_role != role:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to add address'
        )

    username = token_payload['username']
    customer = Customer.search_by_username(session=session, username=username)
    added_address = Address.add(session=session, customer_id=customer.id, address=address.address)

    return added_address


@router.delete('/{address_id}', response_model=AddressForRead)
def deletion(customer_token: str, address_id: int, session: Session = Depends(get_session)):
    token_payload = check_token(token=customer_token)
    token_role = token_payload['role']
    if token_role != role:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to delete address'
        )

    username = token_payload['username']
    customer = Customer.search_by_username(session=session, username=username)

    deleted_address = Address.delete(session=session, customer_id=customer.id, address_id=address_id)
    if deleted_address is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='An address with this id not found'
        )

    return deleted_address


@router.get('', response_model=[AddressForRead])
def show_all(customer_token: str, session: Session = Depends(get_session)):
    token_payload = check_token(token=customer_token)
    token_role = token_payload['role']
    if token_role != role:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to see addresses of this customer'
        )

    username = token_payload['username']
    customer = Customer.search_by_username(session=session, username=username)
    addresses = Address.show_all(session=session, customer_id=customer.id)

    return addresses


@router.get('/{address_id}', response_model=AddressForRead)
def show_specific(customer_token: str, address_id: int, session: Session = Depends(get_session)):
    token_payload = check_token(token=customer_token)
    token_role = token_payload['role']
    if token_role != role:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to see addresses of this customer'
        )

    username = token_payload['username']
    customer = Customer.search_by_username(session=session, username=username)
    address = Address.search(session=session, customer_id=customer.id, address_id=address_id)

    if address is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='An address with this id not found'
        )

    return address

