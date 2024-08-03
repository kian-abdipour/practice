from fastapi import APIRouter, HTTPException, status, Depends, Header

from sqlalchemy.orm import Session

from restaurant.scheme.cart import CartForRead, CartItemForCreate, CartItemForRead
from restaurant.model.cart_item import CartItem
from restaurant.model.cart import Cart
from restaurant.model.item import Item
from restaurant.database import get_session
from restaurant.authentication import check_token
from restaurant.custom_exception import OutOfStockError
from restaurant.model.helper import Role

from typing import Annotated, List

from copy import deepcopy

router = APIRouter(
    prefix='/carts',
    tags=['cart']
)


@router.post('/item', response_model=CartItemForRead)
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
    cart_item_in_database = CartItem.search_by_item_id(session=session, item_id=item.id, cart_id=cart.id)
    if cart_item_in_database is not None:
        if (cart_item_in_database.quantity + cart_item.quantity) > item.stock:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Stock of {item.name} with id {item.id} is {item.stock}'
                       f' and you want {cart_item.quantity + cart_item_in_database.quantity}'
            )

    if cart_item.quantity > item.stock:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Stock of {item.name} with id {item.id} is {item.stock} and you want {cart_item.quantity}'
        )

    if cart is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='A customer with this id not found'
        )

    added_cart_item = CartItem.add(
        session=session,
        item_id=cart_item.item_id,
        cart_id=cart.id,
        quantity=cart_item.quantity,
        cart_item_in_database=cart_item_in_database
    )
    return added_cart_item


@router.delete('/{item_id}', response_model=CartItemForRead)
def deletion(customer_token: Annotated[str, Header()], item_id, session: Session = Depends(get_session)):
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

    return deleted_cart_item


@router.put('/{item_id}', response_model=CartItemForRead)
def decrease_quantity(
        customer_token: Annotated[str, Header()],
        item_id: int,
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

    if Cart.search_cart_by_id(session=session, cart_id=cart.id) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='A cart by this id not found'
        )

    if Item.search_by_id(session=session, item_id=item_id) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='An item by this id not found'
        )

    updated_cart_item = CartItem.decrease_quantity(session=session, item_id=item_id, cart_id=cart.id)
    if updated_cart_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Item is not in customer cart\'s'
        )

    return updated_cart_item


@router.get('/item_stock')
def check_stock_of_item_in_cart(customer_token: str, session: Session = Depends(get_session)):
    token_payload = check_token(customer_token)

    token_role = token_payload['role']
    if token_role != Role.customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to delete item from cart for customer'
        )

    customer_id = token_payload['id']
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

    return []

