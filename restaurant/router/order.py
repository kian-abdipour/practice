from statistics import quantiles

from fastapi import APIRouter, HTTPException, status, Depends, Header
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from restaurant.scheme.order import OrderForCreate, OrderForRead, OrderFilter
from restaurant.scheme.item import ItemOutOfStock
from restaurant.database import get_session
from restaurant.model import Order, OrderItem
from restaurant.router.cart import update_stock_of_item
from restaurant.model.cart import Cart, CartItem
from restaurant.custom_exception import OutOfStockError
from restaurant.authentication import check_token
from restaurant.model.helper import Role, State
from restaurant.router.payment import addition_payment
from restaurant.router.payment import addition_payment

from sqlalchemy.orm import Session

from typing import Annotated, List

from fastapi_pagination import paginate, LimitOffsetPage, add_pagination

from fastapi_filter import FilterDepends


router = APIRouter(
    prefix='/orders',
    tags=['order']
)


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

#    items_out_of_stock = check_stock_of_item_in_cart(customer_token=customer_token, session=session)
#    if len(items_out_of_stock) > 0:
#
#        return items_out_of_stock
    customer_id = token_payload['id']

    items = Cart.show_item_in_a_cart(session=session, customer_id=customer_id, item_filter=None)
    cart_items = Cart.show_item_identifiers_in_a_cart(session=session, customer_id=customer_id)
    if len(cart_items) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Customer does\'nt hase any item in its cart'
        )

    else:
        amount = 0
        for cart_item in cart_items:
            amount = amount + cart_item.total_amount

    customer_id = token_payload['id']

    added_payment = addition_payment(
        customer_id=customer_id,
        payment_state='Successful',
        payment_type=order.payment_type,
        discount_code=order.discount_code,
        amount = amount,
        session=session
    )
    session.commit()
    session.refresh(added_payment)

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

    session.commit()
    session.refresh(added_order)

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
                detail=f'The item with id {cart_item.id} is out of stock'
            )

        CartItem.delete(session=session, item_id=cart_item.item_id, cart_id=cart_item.cart_id)

    for item in items:
        update_stock_of_item(item=item, session=session)

    session.commit()
    return added_order


@router.put('/{order_id}', response_model=OrderForRead)
def confirm_order(
        admin_token: Annotated[str, Header()],
        order_id: int,
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


@router.get('', response_model=LimitOffsetPage[OrderForRead])
def get(
        customer_or_admin_token: Annotated[str, Header()],
        order_filter: OrderFilter = FilterDepends(OrderFilter),
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
        if order_filter.id is not None:
            order = show_specific_order(order_id=order_filter.id, session=session)
            order_dict = order.__dict__
            jsonable_order = jsonable_encoder(order_dict)

            return JSONResponse(status_code=200, content=jsonable_order)

        elif order_filter.state is not None:
            orders = Order.show_by_state_for_admin(state=order_filter.state, session=session, order_filter=order_filter)

            return paginate(orders)

        else:
            orders = Order.show_all_for_admin(session=session, order_filter=order_filter)

            return paginate(orders)

    if token_role == Role.customer:
        if order_filter.id is not None:
            order = Order.search_by_customer_id_and_order_id(
                session=session, customer_id=customer_id, order_id=order_filter.id
            )
            if order is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='This customer does not have any order with this id'
                )

            return order

        elif order_filter.state is not None:
            orders = Order.show_by_state_for_customer(
                session=session,
                customer_id=customer_id,
                state=order_filter.state,
                order_filter=order_filter
            )

            return paginate(orders)

        else:
            orders = Order.show_all_for_customer(session=session, customer_id=customer_id, order_filter=order_filter)

            return paginate(orders)

