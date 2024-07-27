from fastapi import APIRouter, HTTPException, status, Depends

from sqlalchemy.orm import Session

from restaurant.authentication import check_token
from restaurant.model import Item
from restaurant.scheme.item import ItemForCreate, ItemForRead
from restaurant.database import get_session


router = APIRouter(
    prefix='/items',
    tags=['item']
)

admin_role = 'admin'
customer_role = 'customer'


@router.post('', response_model=ItemForCreate)
def addition(customer_or_admin_token: str, item: ItemForCreate, session: Session = Depends(get_session)):
    token_payload = check_token(token=customer_or_admin_token)

    token_role = token_payload['role']
    if token_role != admin_role and token_role != customer_role:
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


@router.get('', response_model=[ItemForRead])
def show_all(customer_or_admin_token: str, session: Session = Depends(get_session)):
    token_payload = check_token(token=customer_or_admin_token)

    token_role = token_payload['role']
    if token_role != admin_role and token_role != customer_role:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to see item'
        )

    result = Item.show_all(session=session)

    return result


@router.get('{item_id}', response_model=ItemForRead)
def show_specific_by_id(customer_or_admin_token: str, item_id: int, session: Session = Depends(get_session)):
    token_payload = check_token(token=customer_or_admin_token)

    token_role = token_payload['role']
    if token_role != admin_role and token_role != customer_role:
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


@router.get('item_name', response_model=ItemForRead)
def show_specific_by_name(customer_or_admin_token: str, name: str, session: Session = Depends(get_session)):
    token_payload = check_token(token=customer_or_admin_token)

    token_role = token_payload['role']
    if token_role != admin_role and token_role != customer_role:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to see item'
        )

    item = Item.search_by_name(session=session, name=name)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Item with this name not found'
        )
