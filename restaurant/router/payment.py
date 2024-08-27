from fastapi import APIRouter, HTTPException, status, Depends, Header
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from restaurant.scheme.payment import PaymentForRead, PaymentFilter
from restaurant.model import Payment, Discount, DiscountHistory
from restaurant.database import get_session
from restaurant.custom_exception import DisposableDiscountError, StartDateDiscountError, ExpireDateDiscountError, \
                                         UsageLimitationDiscountError, UsedDiscountError
from restaurant.model.helper import State, Role
from restaurant.authentication import check_token

from sqlalchemy.orm import Session

from typing import Annotated

from fastapi_pagination import paginate, LimitOffsetPage

from fastapi_filter import FilterDepends


router = APIRouter(
    prefix='/payments',
    tags=['payment']

)


#@router.post('', response_model=PaymentForRead)
def addition_payment(
        customer_id,
        payment_state,
        payment_type,
        discount_code,
        amount,
        session: Session
):
#    if len(cart_items) == 0:
#        raise HTTPException(
#            status_code=statu
#            s.HTTP_400_BAD_REQUEST,
#            detail='Customer does not have any item in it\'s cart'
#        )

#   for cart_item in cart_items:
#        item = Item.search_by_id(session=session, item_id=cart_item.item_id)
#        amount += (item.price * cart_item.quantity)

    if discount_code is not None:
        discount = Discount.search_by_code(session=session, code=discount_code)
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
        state=payment_state,
        type_=payment_type,
        amount=effected_amount,
        customer_id=customer_id
    )

    if added_payment.state == State.successful and discount_code is not None:
        if discount.usage_limitation is not None:
            Discount.usage_limitation = discount.usage_limitation - 1
        DiscountHistory.add(
            session=session,
            discount_id=discount.id,
            payment_id=added_payment.id,
            base_amount=amount,
            affected_amount=added_payment.amount
        )

    session.flush()
    session.refresh(added_payment)

    return added_payment


@router.get('', response_model=LimitOffsetPage[PaymentForRead])
def search(
        admin_token: Annotated[str, Header()],
        payment_filter: PaymentFilter = FilterDepends(PaymentFilter),
        session: Session = Depends(get_session)
):
    token_payload = check_token(admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to see payments'
        )

    if payment_filter.id is not None:
        payment = Payment.search_by_id(session=session, payment_id=payment_filter.id)
        if payment is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='A payment with this id not found'
            )
        payment_dict = payment.__dict__
        jsonable_payment = jsonable_encoder(payment_dict)

        return JSONResponse(status_code=200, content=jsonable_payment)

    else:
        payments = Payment.show_all(session=session, payment_filter=payment_filter)

        return paginate(payments)

