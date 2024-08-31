from fastapi import APIRouter, HTTPException, status, Depends, Header

from sqlalchemy.orm import Session

from restaurant.scheme.cart import CartItemForUpdate, CartItemForRead, CartItemForCreate
from restaurant.model.cart_item import CartItem
from restaurant.model.cart import Cart
from restaurant.model.item import Item
from restaurant.database import get_session
from restaurant.authentication import check_token
from restaurant.custom_exception import OutOfStockError, ItemNotInCartError
from restaurant.model.helper import Role
from restaurant.scheme.cart import CartItemFilter

from typing import Annotated, List

from fastapi_pagination import paginate, LimitOffsetPage, add_pagination

from fastapi_filter import FilterDepends


router = APIRouter(
    prefix='/carts',
    tags=['cart']
)
add_pagination(router)


@router.post('', response_model=CartItemForRead)
def addition_item_to_cart(
        customer_token: Annotated[str, Header()],
        cart_item: CartItemForCreate,
        session: Session = Depends(get_session)
):
    token_payload = check_token(customer_token)
    customer_id = token_payload['id']

    token_role = token_payload['role']
    if token_role != Role.customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to add item to cart for customer'
        )

    item = Item.search_by_id(session=session, item_id=cart_item.item_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='An item with this id not found'
        )

    if item.stock == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Stock of {item.name} with id {item.id} is out of stock'
        )

    cart = Cart.search_cart_by_customer(session=session, customer_id=customer_id)

    cart_item_in_database = CartItem.search_by_item_id(session=session, cart_id=cart.id, item_id=item.id)
    if cart_item_in_database is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='This item is already added to cart of this customer'
        )

    added_cart_item = CartItem.add(
        session=session,
        item_id=item.id,
        cart_id=cart.id,
        quantity=1,
    )

    session.commit()

    return added_cart_item


@router.delete('/{item_id}', response_model=CartItemForRead)
def delete(customer_token: Annotated[str, Header()], item_id, session: Session = Depends(get_session)):
    token_payload = check_token(customer_token)

    token_role = token_payload['role']
    if token_role != Role.customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to delete item from cart for customer'
        )

    if Item.search_by_id(session=session, item_id=item_id) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='An item by this id not found'
        )

    customer_id = token_payload['id']
    cart = Cart.search_cart_by_customer(session=session, customer_id=customer_id)

    deleted_cart_item = CartItem.delete(session=session, item_id=item_id, cart_id=cart.id)
    if deleted_cart_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='An item is not in this cart'
        )

    session.commit()

    return deleted_cart_item


@router.put('', response_model=CartItemForRead)
def update_quantity(
        customer_token: Annotated[str, Header()],
        cart_item: CartItemForUpdate,
        session: Session = Depends(get_session)
):
    token_payload = check_token(customer_token)

    token_role = token_payload['role']
    if token_role != Role.customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to delete item from cart for customer'
        )

    customer_id = token_payload['id']
    cart = Cart.search_cart_by_customer(session=session, customer_id=customer_id)

    item = Item.search_by_id(session=session, item_id=cart_item.item_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='An item by this id not found'
        )

    try:
        updated_cart_item = CartItem.update_quantity(
            session=session,
            item_id=cart_item.item_id,
            cart_id=cart.id,
            quantity=cart_item.quantity,
            item=item
        )

    except OutOfStockError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='The item is out of stock'
        )

    except ItemNotInCartError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Item is not in cart, first you should add item'
        )

    session.commit()

    return updated_cart_item


#@router.get('/item-stock', response_model=ItemOutOfStock)
def update_stock_of_item(item, session: Session):
    cart_items = CartItem.show_cart_item_by_item_id(session=session, item_id=item.id)

    for cart_item in cart_items:
        if item.stock == 0:
            CartItem.delete(session=session, item_id=cart_item.item_id, cart_id=cart_item.cart_id)

        else:
            if cart_item.quantity > item.stock:
                cart_item.quantity = item.stock


@router.get('/items', response_model=LimitOffsetPage[CartItemForRead])
def get_items_in_customer_cart(
        customer_token: Annotated[str, Header()],
        cart_item_filter: CartItemFilter = FilterDepends(CartItemFilter),
        session: Session = Depends(get_session)
):
    token_payload = check_token(customer_token)

    token_role = token_payload['role']
    if token_role != Role.customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to items in the cart of customer'
        )

    customer_id = token_payload['id']
    cart = Cart.search_cart_by_customer(session=session, customer_id=customer_id)

    cart_items = CartItem.search_by_cart_id(session=session, cart_id=cart.id, cart_item_filter=cart_item_filter)

    return paginate(cart_items)

