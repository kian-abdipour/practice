from fastapi import APIRouter, HTTPException, status, Depends, Header

from restaurant.scheme.order import OrderForCreate, OrderForRead
from restaurant.database import get_session
from restaurant.model import Order, OrderItem
from restaurant.model.cart import Cart, CartItem
from restaurant.custom_exception import OutOfStockError
from restaurant.authentication import check_token
from restaurant.model.helper import Role

from sqlalchemy.orm import Session

from typing import Annotated


router = APIRouter(
    prefix='/orders',
    tags=['order']
)


@router.post('', response_model=OrderForRead)
def addition(admin_token: Annotated[str, Header()], order: OrderForCreate, session: Session = Depends(get_session)):
    token_payload = check_token(token=admin_token)

    token_role = token_payload['role']
    if token_role != Role.customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to add order'
        )

    cart_items = Cart.show_item_identifiers_in_a_cart(session=session, customer_id=order.customer_id)
    if cart_items is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='A customer with this id not found'
        )

    added_order = Order.add(
        session=session,
        state=order.state,
        delivery_type=order.delivery_type,
        desk_number=order.desk_number,
        description=order.description,
        address_id=order.address_id,
        customer_id=order.customer_id
    )

    for cart_item in cart_items:
        try:
            OrderItem.add(
                session=session,
                order_id=added_order.id,
                item_id=cart_item.item_id,
                quantity=cart_item.quantity,
                unit_amount=cart_item.unit_amount,
                total_amount=cart_item.total_amount
            )

        except OutOfStockError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'The item with id {cart_item.item_id} is out of stock'
            )

    return added_order


@router.get('/?state=Waiting to confirmation')
def show_all_waiting_to_confirm(
        customer_or_admin_token: Annotated[str, Header()], session: Session = Depends(get_session)
):
    token_payload = check_token(token=customer_or_admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin and token_role != Role.customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to see item'
        )

    orders = Order.show_all_waiting_to_confirm(session=session)

    return orders


@router.put('{order_id}', response_model=OrderForRead)
def confirm_order(
        admin_token: Annotated[str, Header()],
        order_id: str,
        session: Session = Depends(get_session)
):
    token_payload = check_token(token=admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to see item'
        )

    confirmed_order = Order.confirm(session=session, order_id=order_id)
    if confirmed_order is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='An order with this id not found'
        )

    return confirmed_order

