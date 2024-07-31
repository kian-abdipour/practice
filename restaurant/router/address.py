from fastapi import APIRouter, Depends, HTTPException, status, Header

from restaurant.database import get_session
from restaurant.authentication import check_token
from restaurant.model import Address, Customer
from restaurant.scheme.address import AddressForAddition, AddressForRead  # AllAddressForRead
from restaurant.model.helper import Role

from sqlalchemy.orm import Session

from typing import Annotated, List


router = APIRouter(
    prefix='/addresses',
    tags=['address']
)


@router.post('', response_model=AddressForRead)
def addition(customer_token: Annotated[str, Header()],
             address: AddressForAddition,
             session: Session = Depends(get_session)):

    token_payload = check_token(token=customer_token)
    token_role = token_payload['role']
    if token_role != Role.customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to add address'
        )

    customer_id = token_payload['id']
    added_address = Address.add(session=session, customer_id=customer_id, address=address.address)

    return added_address


@router.delete('/{address_id}', response_model=AddressForRead)
def deletion(customer_token: Annotated[str, Header()], address_id: int, session: Session = Depends(get_session)):
    token_payload = check_token(token=customer_token)
    token_role = token_payload['role']
    if token_role != Role.customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to delete address'
        )

    customer_id = token_payload['id']
    deleted_address = Address.delete(session=session, customer_id=customer_id, address_id=address_id)
    if deleted_address is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='An address with this id not found'
        )

    return deleted_address


@router.get('', response_model=List[AddressForRead])
def show_all(customer_token: Annotated[str, Header()], session: Session = Depends(get_session)):
    token_payload = check_token(token=customer_token)
    token_role = token_payload['role']
    if token_role != Role.customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to see addresses of this customer'
        )

    customer_id = token_payload['id']
    addresses = Address.show_all(session=session, customer_id=customer_id)

    return addresses


@router.get('/{address_id}', response_model=AddressForRead)
def show_specific(customer_token: Annotated[str, Header()], address_id: int, session: Session = Depends(get_session)):
    token_payload = check_token(token=customer_token)
    token_role = token_payload['role']
    if token_role != Role.customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to see addresses of this customer'
        )

    customer_id = token_payload['id']
    address = Address.search(session=session, customer_id=customer_id, address_id=address_id)

    if address is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='An address with this id not found'
        )

    return address

