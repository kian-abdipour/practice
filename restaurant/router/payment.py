from fastapi import APIRouter, HTTPException, status, Depends, Header

from restaurant.scheme.payment import PaymentForRead, PaymentForCreate
from restaurant.model import Payment, Discount, DiscountHistory
from restaurant.database import get_session
from restaurant.custom_exception import DisposableDiscountError, StartDateDiscountError, ExpireDateDiscountError,\
                                         UsageLimitationDiscountError
from restaurant.model.helper import State, Role
from restaurant.authentication import check_token

from sqlalchemy.orm import Session

from typing import Annotated


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
            detail='You don\'t have access to see item'
        )

    if payment.discount_code is not None:
        discount = Discount.search_by_code(session=session, code=payment.discount_code)
        if discount is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='A discount by this id not found'
            )

        try:
            amount = discount.apply_discount(session=session, discount=discount)

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
        amount = payment.amount

    added_payment = Payment.add(
        session=session,
        state=payment.state,
        type_=payment.type,
        amount=amount,
        order_id=payment.order_id,
        customer_id=payment.customer_id
    )

    if added_payment.state == State.successful and payment.discount_code is not None:
        Discount.decrease_usage_limitation(session=session, discount_id=discount.id)
        DiscountHistory.add(
            session=session,
            discount_id=discount.id,
            payment_id=added_payment.id,
            base_amount=payment.amount,
            affected_amount=added_payment.amount
        )

    return added_payment

