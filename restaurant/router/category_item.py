from fastapi import APIRouter, HTTPException, status, Depends, Header

from restaurant.scheme.category_item import CategoryItemForRead, AdditionItemToCategory, DeleteItemFromCategory
from restaurant.database import get_session
from restaurant.model import Category, CategoryItem, Item
from restaurant.authentication import check_token
from restaurant.model.helper import Role

from sqlalchemy.orm import Session

from typing import Annotated

router = APIRouter(
    prefix='/category_items',
    tags=['category_item']
)


@router.post('', response_model=AdditionItemToCategory)
def addition(
        admin_token: Annotated[str, Header()],
        category_item: AdditionItemToCategory,
        session: Session = Depends(get_session)
):
    token_payload = check_token(token=admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to add item to category'
        )

    if Category.search_by_id(session=session, category_id=category_item.category_id) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='A category with this id not found'
        )

    if Item.search_by_id(session=session, item_id=category_item.item_id) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='An item with this id not found'
        )

    added_category_item = CategoryItem.add(
        session=session,
        category_id=category_item.category_id,
        item_id=category_item.item_id
    )
    if added_category_item is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='This item already is in this category'
        )

    return added_category_item


@router.get('/{category_id}', response_model=CategoryItemForRead)
def show_item_side(
        admin_token_or_customer_token: Annotated[str, Header()],
        category_id: int,
        session: Session = Depends(get_session)
):
    token_payload = check_token(token=admin_token_or_customer_token)

    token_role = token_payload['role']
    if token_role != Role.admin and token_role != Role.customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access see item of category'
        )

    category_in_database = Category.search_by_id(session=session, category_id=category_id)
    if category_in_database is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='A category with this id not found'
        )

    item_in_category = CategoryItem.show_item_side(session=session, category_id=category_id)
    category = CategoryItemForRead(id=category_id, name=category_in_database.name, items=item_in_category)
    
    return category


@router.delete('', response_model=DeleteItemFromCategory)
def delete(
        admin_token: Annotated[str, Header()],
        category_item: DeleteItemFromCategory,
        session: Session = Depends(get_session)
):
    token_payload = check_token(token=admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to delete item from category'
        )

    category = Category.search_by_id(session=session, category_id=category_item.category_id)
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='A category with this id not found'
        )

    item = Item.search_by_id(session=session, item_id=category_item.item_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Item with this id not found'
        )

    deleted_category_item = CategoryItem.delete(
        session=session,
        category_id=category_item.category_id,
        item_id=category_item.item_id
    )
    if deleted_category_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='This Item is not in this category'
        )

    return deleted_category_item

