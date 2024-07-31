from fastapi import APIRouter, Depends, HTTPException, status, Header


from restaurant.scheme.category import CategoryForCreate, CategoryForRead
from restaurant.database import get_session
from restaurant.model import Category
from restaurant.authentication import check_token
from restaurant.model.helper import Role

from sqlalchemy.orm import Session

from typing import Annotated, List

router = APIRouter(
    prefix='/categories',
    tags=['Category']
)


@router.post('', response_model=CategoryForRead)
def addition(
        admin_token: Annotated[str, Header()],
        category: CategoryForCreate,
        session: Session = Depends(get_session)
):
    token_payload = check_token(token=admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to add category'
        )

    result = Category.search_by_name(session=session, name=category.name)

    if result is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='A category with this name already exist'
        )

    added_category = Category.add(session=session, name=category.name)
    return added_category


@router.get('', response_model=List[CategoryForRead])
def show_all(admin_token: Annotated[str, Header()], session: Session = Depends(get_session)):
    token_payload = check_token(admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to see category'
        )
    result = Category.show_all(session=session)

    return result


@router.get('/{category_id}', response_model=CategoryForRead)
def show_specific(
        admin_token: Annotated[str, Header()],
        category_id: int,
        session: Session = Depends(get_session)
):
    token_payload = check_token(admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to see category'
        )
    result = Category.search_by_id(session=session, category_id=category_id)

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='A category with this id not found'
        )

    return result


@router.delete('/{category_id}', response_model=CategoryForRead)
def delete(admin_token: Annotated[str, Header()], category_id: int, session: Session = Depends(get_session)):
    token_payload = check_token(admin_token)

    token_role = token_payload['role']
    if token_role != Role.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to delete category'
        )

    result = Category.delete(session=session, id_=category_id)
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='A category with this id not found'
        )

    return result

