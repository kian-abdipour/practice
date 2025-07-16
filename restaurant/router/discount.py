from fastapi import APIRouter, HTTPException, status, Depends, Header
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from restaurant.scheme.discount import DiscountForCreate, DiscountForRead, DiscountForUpdateDisposable, DiscountFilter
from restaurant.database import get_session
from restaurant.authentication import check_token
from restaurant.model.helper import Role
from restaurant.model.discount import Discount

from sqlalchemy.orm import Session

from typing import Annotated

from fastapi_filter import FilterDepends

from fastapi_pagination import paginate, LimitOffsetPage, add_pagination


router = APIRouter(
    prefix='/discounts',
    tags=['discount']
)
add_pagination(router)


@router.post('', response_model=DiscountForRead)
def addition(
        admin_token: Annotated[str, Header()],
        discount: DiscountForCreate,
        session: Session = Depends(get_session)
):
    token_payload = check_token(token=admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to add discount'
        )

    code = Discount.generate_code(session=session)

    added_discount = Discount.add(
        session=session,
        start_date=discount.start_date,
        expire_date=discount.expire_date,
        title=discount.title,
        percent=discount.percent,
        code=code,
        description=discount.description,
        usage_limitation=discount.usage_limitation,
        disposable=discount.disposable,
        one_use=discount.one_use
    )

    session.commit()

    return added_discount


@router.put('/{discount_id}', response_model=DiscountForRead)
def update_disposable(
        admin_token: Annotated[str, Header()],
        discount_id: int,
        updated_discount: DiscountForUpdateDisposable,
        session: Session = Depends(get_session)
):
    token_payload = check_token(token=admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to add discount'
        )

    discount = Discount.search_by_id(session=session, discount_id=discount_id)
    if discount is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Discount with this id not found'
        )

    updated_discount = Discount.update_disposable(
        session=session,
        discount_id=discount.id,
        disposable=updated_discount.disposable
    )

    session.commit()

    return updated_discount


@router.get('', response_model=LimitOffsetPage[DiscountForRead])
def get(
        admin_token: Annotated[str, Header()],
        discount_filter: DiscountFilter = FilterDepends(DiscountFilter),
        session: Session = Depends(get_session)
):
    token_payload = check_token(admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to se discount'
        )

    if discount_filter.id is not None:
        discount = Discount.search_by_id(session=session, discount_id=discount_filter.id)
        if discount is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Discount with this id not found'
            )
        discount_dict = discount.__dict__
        jsonable_discount = jsonable_encoder(discount_dict)

        return JSONResponse(status_code=200, content=jsonable_discount)

    else:
        discounts = Discount.show_all(session=session, discount_filter=discount_filter)

        return paginate(discounts)

