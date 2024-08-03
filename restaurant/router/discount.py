from fastapi import APIRouter, HTTPException, status, Depends, Header

from restaurant.scheme.discount import DiscountForCreate, DiscountForRead
from restaurant.database import get_session
from restaurant.authentication import check_token
from restaurant.model.helper import Role
from restaurant.model.discount import Discount

from sqlalchemy.orm import Session

from typing import List, Annotated

router = APIRouter(
    prefix='/discounts',
    tags=['discount']
)


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
        disposable=discount.disposable
    )
    return added_discount


@router.put('/{Discount_id}/{disposable}', response_model=DiscountForRead)
def update_disposable(
        admin_token: Annotated[str, Header()],
        discount_code,
        disposable,
        session: Session = Depends(get_session)
):
    token_payload = check_token(token=admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to add discount'
        )

    discount = Discount.search_by_code(session=session, code=discount_code)
    if discount is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Discount with this code not found'
        )

    updated_discount = Discount.update_disposable(session=session, discount_id=discount.id, disposable=disposable)
#    if updated_discount.disposable is False:
#        updated_discount.disposable = 'false'
#
#    if updated_discount.disposable is True:
#        updated_discount.disposable = 'true'

    return updated_discount


@router.get('', response_model=List[DiscountForRead])
def show_all(admin_token: Annotated[str, Header()], session: Session = Depends(get_session)):
    token_payload = check_token(token=admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to see discounts'
        )

    discounts = Discount.show_all(session=session)

    return discounts

