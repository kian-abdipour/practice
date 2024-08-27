from fastapi import APIRouter, HTTPException, status, Depends, Header
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

from restaurant.authentication import check_token
from restaurant.model import Item, CategoryItem, Category
from restaurant.scheme.item import ItemForCreate, ItemForRead, ItemFilter
from restaurant.database import get_session
from restaurant.model.helper import Role

from typing import Annotated

from fastapi_pagination import paginate, LimitOffsetPage, add_pagination
from fastapi_filter import FilterDepends


router = APIRouter(
    prefix='/items',
    tags=['item']
)
add_pagination(router)


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

    result = Item.search_by_name(session=session, item_name=item.name)
    if result is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='An item with this name is already exist choose another one'
        )

    category = Category.search_by_id(session=session, category_id=item.category_id)
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='A category with this id not found'
        )

    added_item = Item.add(
        session=session, name=item.name,
        country=item.country, price=item.price,
        stock=item.stock, description=item.description
    )

    CategoryItem.add(session=session, category_id=category.id, item_id=added_item.id)

    return added_item


@router.get('', response_model=LimitOffsetPage[ItemForRead])
def get(
        customer_or_admin_token: Annotated[str, Header()],
        item_filter: ItemFilter = FilterDepends(ItemFilter),
        session: Session = Depends(get_session)
):
    token_payload = check_token(token=customer_or_admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin and token_role != Role.customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to see item'
        )

    if item_filter.id is not None:
        item = Item.search_by_id(session=session, item_id=item_filter.id)
        if item is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='An item with this id not found'
            )
        item_dict = item.__dict__
        print(item_dict)
        jsonable_item = jsonable_encoder(item_dict)

        return JSONResponse(status_code=200, content=jsonable_item)

    elif item_filter.name is not None:
        item = Item.search_by_name(session=session, item_name=item_filter.name)
        if item is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='An item with this name not found'
            )
        item_dict = item.__dict__
        print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>: {item_dict}")
        jsonable_item = jsonable_encoder(item_dict)

        return JSONResponse(status_code=200, content=jsonable_item)

    elif item_filter.id is None and item_filter.name is None:
        items = Item.show_all(session=session, item_filter=item_filter)

        return paginate(items)

