from fastapi import APIRouter, Depends, HTTPException, status, Header
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from restaurant.scheme.category import CategoryForCreate, CategoryForRead, CategoryFilter
from restaurant.scheme.category_item import CategoryItemForRead, DeleteItemFromCategory, \
    AdditionItemToCategoryForRead, AdditionItemToCategory
from restaurant.scheme.item import ItemInCategoryFilter, ItemForRead
from restaurant.database import get_session
from restaurant.model import Category, CategoryItem, Item
from restaurant.authentication import check_token
from restaurant.model.helper import Role

from sqlalchemy.orm import Session

from typing import Annotated, List

from fastapi_pagination import LimitOffsetPage, paginate, add_pagination

from fastapi_filter import FilterDepends


router = APIRouter(
    prefix='/categories',
    tags=['Category']
)
add_pagination(router)


@router.post('', response_model=CategoryForRead)
def addition(
        admin_token: Annotated[str, Header()],
        category: CategoryForCreate,
        session: Session = Depends(get_session)
):
    token_payload = check_token(token=admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to add category'
        )

    result = Category.search_by_name(session=session, name=category.name)

    if result is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='A category with this name already exist'
        )

    added_category = Category.add(session=session, name=category.name)
    return added_category


@router.get('', response_model=LimitOffsetPage[CategoryForRead])
def get(
        admin_token_or_customer_token: Annotated[str, Header()],
        category_filter: CategoryFilter = FilterDepends(CategoryFilter),
        session: Session = Depends(get_session)
):
    token_payload = check_token(admin_token_or_customer_token)

    token_role = token_payload['role']
    if token_role != Role.admin and token_role != Role.customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to see category'
        )

    if category_filter.id is not None:
        category = Category.search_by_id(session=session, category_id=category_filter.id)
        if category is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='A category with this id not found'
            )
        category_dict = category.__dict__
        jsonable_category = jsonable_encoder(category_dict)

        return JSONResponse(status_code=200, content=jsonable_category)

    elif category_filter.name is not None:
        category = Category.search_by_name(session=session, name=category_filter.name)
        if category is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='A category with this name not found'
            )
        category_dict = category.__dict__
        jsonable_category = jsonable_encoder(category_dict)

        return JSONResponse(status_code=200, content=jsonable_category)

    else:
        categories = Category.show_all(session=session, category_filter=category_filter)

        return paginate(categories)


@router.delete('/{category_id}', response_model=CategoryForRead)
def delete(admin_token: Annotated[str, Header()], category_id: int, session: Session = Depends(get_session)):
    token_payload = check_token(admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to delete category'
        )

    result = Category.delete(session=session, id_=category_id)
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='A category with this id not found'
        )

    return result


@router.get('/{category_id}/items', response_model=LimitOffsetPage[ItemForRead])
def get_items_in_category(
        admin_token_or_customer_token: Annotated[str, Header()],
        category_item_filter: ItemInCategoryFilter = FilterDepends(ItemInCategoryFilter),
        session: Session = Depends(get_session)
):
    token_payload = check_token(token=admin_token_or_customer_token)

    token_role = token_payload['role']
    if token_role != Role.admin and token_role != Role.customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access see item of category'
        )

    category_in_database = Category.search_by_id(session=session, category_id=category_item_filter.category_id)
    if category_in_database is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='A category with this id not found'
        )

    item_in_category = CategoryItem.show_item_side(
        session=session,
        category_id=category_item_filter.category_id,
        category_item_filter=category_item_filter
    )

    return paginate(item_in_category)


@router.post('/{category_id}/items', response_model=AdditionItemToCategoryForRead)
def addition_item_to_category(
        admin_token: Annotated[str, Header()],
        category_id: int,
        item: AdditionItemToCategory,
        session: Session = Depends(get_session)
):
    token_payload = check_token(token=admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to add item to category'
        )

    if Category.search_by_id(session=session, category_id=category_id) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='A category with this id not found'
        )

    if Item.search_by_id(session=session, item_id=item.item_id) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='An item with this id not found'
        )

    added_category_item = CategoryItem.add(
        session=session,
        category_id=category_id,
        item_id=item.item_id
    )
    if added_category_item is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='This item already is in this category'
        )

    return added_category_item


@router.delete('/{category_id}/items/{item_id}', response_model=DeleteItemFromCategory)
def delete_item_from_category(
        admin_token: Annotated[str, Header()],
        category_id: int,
        item_id: int,
        session: Session = Depends(get_session)
):
    token_payload = check_token(token=admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to delete item from category'
        )

    category = Category.search_by_id(session=session, category_id=category_id)
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='A category with this id not found'
        )

    item = Item.search_by_id(session=session, item_id=item_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Item with this id not found'
        )

    deleted_category_item = CategoryItem.delete(
        session=session,
        category_id=category_id,
        item_id=item_id
    )
    if deleted_category_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='This Item is not in this category'
        )

    return deleted_category_item

