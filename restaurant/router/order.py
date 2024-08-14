from fastapi import APIRouter, HTTPException, status, Depends, Header

from restaurant.scheme.order import OrderForCreate, OrderForRead
from restaurant.database import get_session
from restaurant.model import Order, OrderItem
from restaurant.model.cart import Cart, CartItem
from restaurant.custom_exception import OutOfStockError
from restaurant.authentication import check_token
from restaurant.model.helper import Role, State
from restaurant.router.payment import addition_payment
from restaurant.router.payment import addition_payment

from sqlalchemy.orm import Session

from typing import Annotated, List


router = APIRouter(
    prefix='/orders',
    tags=['order']
)


def show_by_state(
        state: str,
        session: Session = Depends(get_session)
):
    orders = Order.show_by_state_for_admin(session=session, state=state)

    return orders


def show_specific_order(order_id: int, session: Session = Depends(get_session)):
    order = Order.search_by_id(session=session, order_id=order_id)
    if order is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='An order with this id not found'
        )

    return order


def show_all_orders_for_customer(
        customer_token: Annotated[str, Header()],
        session: Session = Depends(get_session)
):
    token_payload = check_token(token=customer_token)

    token_role = token_payload['role']
    if token_role != Role.customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to see orders'
        )

    customer_id = token_payload['id']
    orders = Order.search_by_customer_id(session=session, customer_id=customer_id)

    return orders


def show_all_orders_for_admin(session):
    orders = Order.show_all_for_admin(session=session)

    return orders


def show_specific_order_for_customer(session, order_id, customer_id):
    order = Order.search_by_customer_id_and_order_id(session=session, order_id=order_id, customer_id=customer_id)

    if order is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='This customer does not have any order with this id'
        )

    return order


def show_by_state_for_customer(session: Session, customer_id, order_state):
    orders = Order.show_by_state_for_customer(session=session, customer_id=customer_id, state=order_state)

    return orders


def show_all_for_customer(session, customer_id):
    orders = Order.show_all_for_customer(session=session, customer_id=customer_id)

    return orders


@router.post('', response_model=OrderForRead)
def addition_order(
        customer_token: Annotated[str, Header()],
        order: OrderForCreate,
        session: Session = Depends(get_session)
):
    token_payload = check_token(token=customer_token)

    token_role = token_payload['role']
    if token_role != Role.customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to add order'
        )

    customer_id = token_payload['id']

    cart_items = Cart.show_item_identifiers_in_a_cart(session=session, customer_id=customer_id)
    added_payment = addition_payment(
        customer_id=customer_id,
        payment_state='Successful',
        payment_type=order.payment_type,
        discount_code=order.discount_code,
        cart_items=cart_items,
        session=session
    )
#    if cart_items is None:
#        raise HTTPException(
#            status_code=status.HTTP_404_NOT_FOUND,
#            detail='A customer with this id not found'
#        )

    added_order = Order.add(
        session=session,
        state=State.waiting_to_confirmation,
        delivery_type=order.delivery_type,
        desk_number=order.desk_number,
        description=order.description,
        payment_id=added_payment.id,
        address_id=order.address_id,
        customer_id=customer_id
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

        CartItem.delete(session=session, item_id=cart_item.item_id, cart_id=cart_item.cart_id)

    return added_order


@router.put('/{order_id}', response_model=OrderForRead)
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
            detail='You don\'t have access to confirm order'
        )

    order = Order.search_by_id(session=session, order_id=order_id)
    if order is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='An order with this id not found'
        )

    if order.state == State.confirm_and_finish:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='This order is already confirmed'
        )

    confirmed_order = Order.confirm(session=session, order_id=order_id)
    if confirmed_order is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='An order with this id not found'
        )

    return confirmed_order


@router.get('/orders', response_model=List[OrderForRead] | OrderForRead)
def search(
        customer_or_admin_token: Annotated[str, Header()],
        order_id: int = None,
        order_state: str = None,
        session: Session = Depends(get_session)
):
    token_payload = check_token(customer_or_admin_token)

    token_role = token_payload['role']
    customer_id = token_payload['id']
    if token_role != Role.customer and token_role != Role.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to see orders'
        )

    if token_role == Role.admin:
        if order_id is not None:
            order = show_specific_order(order_id=order_id, session=session)

            return order

        elif order_state is not None:
            orders = show_by_state(state=order_state, session=session)

            return orders

        else:
            orders = show_all_orders_for_admin(session=session)

            return orders

    if token_role == Role.customer:
        if order_id is not None:
            order = show_specific_order_for_customer(session=session, customer_id=customer_id, order_id=order_id)

            return order

        elif order_state is not None:
            orders = show_by_state_for_customer(session=session, customer_id=customer_id, order_state=order_state)

            return orders

        else:
            orders = show_all_for_customer(session=session, customer_id=customer_id)

            return orders

