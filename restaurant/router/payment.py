from fastapi import APIRouter, HTTPException, status, Depends, Header

from restaurant.scheme.payment import PaymentForRead, PaymentForCreate
from restaurant.model import Payment, Discount, DiscountHistory, Item, CartItem, Cart
from restaurant.database import get_session
from restaurant.custom_exception import DisposableDiscountError, StartDateDiscountError, ExpireDateDiscountError, \
                                         UsageLimitationDiscountError, UsedDiscountError
from restaurant.model.helper import State, Role
from restaurant.authentication import check_token

from sqlalchemy.orm import Session

from typing import Annotated, List


router = APIRouter(
    prefix='/payments',
    tags=['payment']

)


@router.post('', response_model=PaymentForRead)
def addition(
        customer_token: Annotated[str, Header()],
        payment: PaymentForCreate,
        session: Session = Depends(get_session)
):
    token_payload = check_token(token=customer_token)

    token_role = token_payload['role']
    if token_role != Role.customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to add payment'
        )

    customer_id = token_payload['id']
    cart = Cart.search_cart_by_customer(session=session, customer_id=customer_id)
    cart_items = CartItem.search_by_cart_id(session=session, cart_id=cart.id)
    if len(cart_items) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Customer does not have any item in it\'s cart'
        )

    amount = 0
    for cart_item in cart_items:
        item = Item.search_by_id(session=session, item_id=cart_item.item_id)
        amount += (item.price * cart_item.quantity)
    print(f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>: {amount}')
    if payment.discount_code is not None:
        discount = Discount.search_by_code(session=session, code=payment.discount_code)
        if discount is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='A discount by this id not found'
            )

        try:
            effected_amount = Discount.apply_discount(
                amount=amount,
                session=session,
                customer_id=customer_id,
                discount=discount
            )

        except UsedDiscountError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Discount is one-use and you used it'
            )

        except DisposableDiscountError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='A discount is disposable'
            )

        except StartDateDiscountError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'You can use discount after {discount.start_date}'
            )

        except ExpireDateDiscountError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='A discount is Expire'
            )

        except UsageLimitationDiscountError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Usage limitation of this discount is finished'
            )

    else:
        effected_amount = amount

    added_payment = Payment.add(
        session=session,
        state=payment.state,
        type_=payment.type,
        amount=effected_amount,
        customer_id=customer_id
    )

    if added_payment.state == State.successful and payment.discount_code is not None:
        if discount.usage_limitation is not None:
            Discount.decrease_usage_limitation(session=session, discount_id=discount.id)
        DiscountHistory.add(
            session=session,
            discount_id=discount.id,
            payment_id=added_payment.id,
            base_amount=amount,
            affected_amount=added_payment.amount
        )

    return added_payment


@router.get('', response_model=List[PaymentForRead])
def show_all(admin_token: Annotated[str, Header()], session: Session = Depends(get_session)):
    token_payload = check_token(admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to see payments'
        )

    payments = Payment.show_all(session=session)

    return payments


@router.get('/{payment_id}', response_model=PaymentForRead)
def show_specific(admin_token: Annotated[str, Header()], payment_id, session: Session = Depends(get_session)):
    token_payload = check_token(admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to see payments'
        )

    payment = Payment.search_by_id(session=session, payment_id=payment_id)
    if payment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='A payment with this id not found'
        )

    return payment

