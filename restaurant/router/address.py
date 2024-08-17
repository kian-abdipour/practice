from fastapi import APIRouter, Depends, HTTPException, status, Header
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from restaurant.database import get_session
from restaurant.authentication import check_token
from restaurant.model import Address, Customer
from restaurant.scheme.address import AddressForAddition, AddressForRead, AddressFilter  # AllAddressForRead
from restaurant.model.helper import Role

from sqlalchemy.orm import Session

from typing import Annotated, List

from fastapi_pagination import LimitOffsetPage, paginate, add_pagination
from fastapi_filter import FilterDepends


router = APIRouter(
    prefix='/addresses',
    tags=['address']
)
add_pagination(router)


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


@router.get('', response_model=LimitOffsetPage[AddressForRead])
def search(
        customer_or_admin_token: str,
        address_filter: AddressFilter = FilterDepends(AddressFilter),
        session: Session = Depends(get_session)
):
    token_payload = check_token(token=customer_or_admin_token)

    token_role = token_payload['role']
    if token_role != Role.customer and token_role != Role.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to see addresses of this customer'
        )

    if token_role == Role.admin:
        if address_filter.id is None:
            pass
            addresses = Address.show_all_for_admin(session=session, address_filter=address_filter)

            return paginate(addresses)

        else:
            address = Address.search_for_admin(
                session=session,
                address_id=address_filter.id,
                address_filter=address_filter
            )
            if address is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='An address with this id not found'
                )
            jsonable_address = jsonable_encoder(address)

            return JSONResponse(status_code=200, content=jsonable_address)

    customer_id = token_payload['id']
    if token_role == Role.customer:
        if address_filter.id is None:
            addresses = Address.show_all_for_customer(
                session=session,
                customer_id=customer_id,
                address_filter=address_filter
            )

            return paginate(addresses)

        else:
            address = Address.search_for_customer(
                session=session,
                address_id=address_filter.id,
                customer_id=customer_id
            )
            if address is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='a customer with this id does not have an address with this id '
                )
            jsonable_address = jsonable_encoder(address)

            return JSONResponse(status_code=200, content=jsonable_address)

