from fastapi import APIRouter, HTTPException, status, Depends

from restaurant.scheme.order import OrderForCreate, OrderForRead
from restaurant.database import get_session
from restaurant.model import Order

router = APIRouter(
    prefix='/orders',
    tags=['order']
)

role = 'customer'


@router.post('', response_model=OrderForRead)
def addition(order: OrderForCreate, session: Depends(get_session)):
    added_order = Order.add(
        session=session,
        state=order.state,
        delivery_type=order.delivery_type,
        desk_number=order.desk_number,
        description=order.description,
        address_id=order.address_id,
        customer_id=order.customer_id
    )



