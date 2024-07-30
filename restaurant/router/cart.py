from fastapi import APIRouter, HTTPException, status, Depends, Header

from sqlalchemy.orm import Session

from restaurant.scheme.cart import CartForRead, CartItemForCreate, CartItemForRead
from restaurant.model.cart_item import CartItem
from restaurant.model.cart import Cart
from restaurant.model.item import Item
from restaurant.database import get_session
from restaurant.authentication import check_token
from restaurant.custom_exception import OutOfStockError

from typing import Annotated


router = APIRouter(
    prefix='/carts',
    tags=['cart']
)

role = 'customer'


@router.post('/item', response_model=CartItemForRead)
def addition_item_to_cart(
        customer_token: Annotated[str, Header()],
        item_id: int,
        cart_id: int,
        quantity: int,
        session: Session = Depends(get_session)
):
    token_payload = check_token(customer_token)

    token_role = token_payload['role']
    if token_role != role:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to add item to cart for customer'
        )

    added_cart_item = CartItem.add(session=session, item_id=item_id, cart_id=cart_id, quantity=quantity)
    return added_cart_item


@router.delete('/{cart_id}/{item_id}', response_model=CartItemForRead)
def deletion(customer_token: Annotated[str, Header()], cart_id, item_id, session: Session = Depends(get_session)):
    token_payload = check_token(customer_token)

    token_role = token_payload['role']
    if token_role != role:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to delete item from cart for customer'
        )

    if Cart.search_cart_by_id(session=session, cart_id=cart_id) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='A cart by this id not found'
        )

    if Item.search_by_id(session=session, item_id=item_id) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='An item by this id not found'
        )

    deleted_cart_item = CartItem.delete(session=session, item_id=item_id, cart_id=cart_id)
    if deleted_cart_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='An item is not in this cart'
        )

    return deleted_cart_item


@router.delete('/{cart_id}/{item_id}', response_model=CartItemForRead)
def decrease_quantity(
        customer_token: Annotated[str, Header()],
        cart_id: int,
        item_id: int,
        session: Session = Depends(get_session)
):
    token_payload = check_token(customer_token)

    token_role = token_payload['role']
    if token_role != role:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to delete item from cart for customer'
        )

    if Cart.search_cart_by_id(session=session, cart_id=cart_id) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='A cart by this id not found'
        )

    if Item.search_by_id(session=session, item_id=item_id) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='An item by this id not found'
        )

    updated_cart_item = CartItem.decrease_quantity(session=session, item_id=item_id, cart_id=cart_id)

    return updated_cart_item


@router.get('/{customer_id}/item_stock')
def check_stock_of_item_in_cart(customer_id: int, session: Session = Depends(get_session)):
    cart_items = Cart.show_item_identifiers_in_a_cart(session=session, customer_id=customer_id)
    for cart_item in cart_items:
        item = Item.search_by_id(session=session, item_id=cart_item.item_id)
        try:
            Item.check_item_stock(item=item, quantity=cart_item.quantity)

        except OutOfStockError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Stock of {item.name} with id {item.id} is {item.stock} and you want {cart_item.quantity}'
            )

