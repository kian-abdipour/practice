from fastapi import APIRouter, HTTPException, status, Depends, Header

from sqlalchemy.orm import Session

from restaurant.authentication import check_token
from restaurant.model import Item
from restaurant.scheme.item import ItemForCreate, ItemForRead
from restaurant.database import get_session
from restaurant.model.helper import Role

from typing import Annotated, List


router = APIRouter(
    prefix='/items',
    tags=['item']
)


@router.post('', response_model=ItemForRead)
def addition(
        admin_token: Annotated[str, Header()],
        item: ItemForCreate,
        session: Session = Depends(get_session)
):
    token_payload = check_token(token=admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to add item'
        )

    result = Item.search_by_name(session=session, name=item.name)
    if result is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='An item with this name is already exist choose another one'
        )

    added_item = Item.add(
        session=session, name=item.name,
        country=item.country, price=item.price,
        stock=item.stock, description=item.description
    )

    return added_item


@router.get('', response_model=List[ItemForRead])
def show_all(customer_or_admin_token: Annotated[str, Header()], session: Session = Depends(get_session)):
    token_payload = check_token(token=customer_or_admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin and token_role != Role.customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to see item'
        )

    result = Item.show_all(session=session)

    return result


@router.get('/{item_id}', response_model=ItemForRead)
def show_specific_by_id(
        customer_or_admin_token: Annotated[str, Header()],
        item_id: int,
        session: Session = Depends(get_session)
):
    token_payload = check_token(token=customer_or_admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin and token_role != Role.customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to see item'
        )

    item = Item.search_by_id(session=session, item_id=item_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Item with this id not found'
        )

    return item


@router.get('/{item_name}', response_model=ItemForRead)
def show_specific_by_name(
        customer_or_admin_token: Annotated[str, Header()],
        item_name: str,
        session: Session = Depends(get_session)
):
    token_payload = check_token(token=customer_or_admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin and token_role != Role.customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to see item'
        )

    item = Item.search_by_name(session=session, name=item_name)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Item with this name not found'
        )

    return item

