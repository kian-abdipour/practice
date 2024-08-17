from fastapi import APIRouter, HTTPException, status, Depends, Header

from sqlalchemy.orm import Session

from restaurant.scheme.cart import CartForRead, CartItemForCreate, CartItemForRead
from restaurant.scheme.item import ItemForRead, ItemInCartFilter
from restaurant.model.cart_item import CartItem
from restaurant.model.cart import Cart
from restaurant.model.item import Item
from restaurant.database import get_session
from restaurant.authentication import check_token
from restaurant.custom_exception import OutOfStockError, ItemNotInCartError
from restaurant.model.helper import Role
from restaurant.scheme.cart import CartItemFilter

from typing import Annotated, List

from copy import deepcopy

from fastapi_pagination import paginate, LimitOffsetPage, add_pagination

from fastapi_filter import FilterDepends


router = APIRouter(
    prefix='/carts',
    tags=['cart']
)
add_pagination(router)


#@router.post('', response_model=CartItemForRead)
#def addition_item_to_cart(
#        customer_token: Annotated[str, Header()],
#        cart_item: CartItemForCreate,
#        session: Session = Depends(get_session)
#):
#    token_payload = check_token(customer_token)
#    customer_id = token_payload['id']
#
#    token_role = token_payload['role']
#    if token_role != Role.customer:
#        raise HTTPException(
#            status_code=status.HTTP_403_FORBIDDEN,
#            detail='You don\'t have access to add item to cart for customer'
#        )
#
#    item = Item.search_by_id(session=session, item_id=cart_item.item_id)
#    if item is None:
#        raise HTTPException(
#            status_code=status.HTTP_404_NOT_FOUND,
#            detail='An item with this id not found'
#        )
#
#    if item.stock == 0:
#        raise HTTPException(
#            status_code=status.HTTP_400_BAD_REQUEST,
#            detail=f'Stock of {item.name} with id {item.id} is out of stock'
#        )
#
#    cart = Cart.search_cart_by_customer(session=session, customer_id=customer_id)
#    cart_item_in_database = CartItem.search_by_item_id(session=session, item_id=item.id, cart_id=cart.id)
#    if cart_item_in_database is not None:
#        if (cart_item_in_database.quantity + cart_item.quantity) > item.stock:
#            raise HTTPException(
#                status_code=status.HTTP_400_BAD_REQUEST,
#                detail=f'Stock of {item.name} with id {item.id} is {item.stock}'
#                       f' and you want {cart_item.quantity + cart_item_in_database.quantity}'
#            )
#
#    if cart_item.quantity > item.stock:
#        raise HTTPException(
#            status_code=status.HTTP_400_BAD_REQUEST,
#            detail=f'Stock of {item.name} with id {item.id} is {item.stock} and you want {cart_item.quantity}'
#        )
#
#    if cart is None:
#        raise HTTPException(
#            status_code=status.HTTP_404_NOT_FOUND,
#            detail='A customer with this id not found'
#        )
#
#    added_cart_item = CartItem.add(
#        session=session,
#        item_id=cart_item.item_id,
#        cart_id=cart.id,
#        quantity=cart_item.quantity,
#        cart_item_in_database=cart_item_in_database
#    )
#    return added_cart_item


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


@router.put('', response_model=CartItemForRead)
def update_quantity(
        customer_token: Annotated[str, Header()],
        cart_item: CartItemForCreate,
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
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Item is not in cart'
        )

    return updated_cart_item


@router.get('/item-stock')
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
    items = []
    items_out_of_stock = []
    for cart_item in cart_items:
        item = Item.search_by_id(session=session, item_id=cart_item.id)
        items.append(item)

        if cart_item.quantity > item.stock:
            items_out_of_stock.append(item)

    return items_out_of_stock


@router.get('/items', response_model=LimitOffsetPage[CartItemForRead])
def show_all(
        customer_token: str,
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

