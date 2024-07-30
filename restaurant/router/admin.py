from fastapi import APIRouter, Depends, HTTPException, status, Header
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from restaurant.scheme.admin import AdminForAddition, AdminForLogin, AdminForRead
from restaurant.database import get_session
from restaurant.model import Admin
from restaurant.authentication import get_hash_password, verify_password, check_token, make_token
from restaurant.model.helper import Role

from sqlalchemy.orm import Session

from datetime import timedelta

from typing import Annotated, List


router = APIRouter(
    prefix='/admins',
    tags=['admin']
)


@router.post('', response_model=AdminForRead)
def addition(
        super_admin_token: Annotated[str, Header()],
        admin: AdminForAddition,
        session: Session = Depends(get_session)
):
    token_payload = check_token(super_admin_token)

    token_role = token_payload['role']
    if token_role != Role.super_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to add admin'
        )

    admin_in_database = Admin.search_by_username(session=session, username=admin.username)
    if admin_in_database is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='This username already exist choose another one'
        )

    super_admin_id = token_payload['id']
    hashed_password = get_hash_password(admin.password)

    added_admin = Admin.add(session=session, first_name=admin.first_name,
                            last_name=admin.last_name, username=admin.username,
                            password=hashed_password, super_admin_id=super_admin_id)

    return added_admin


@router.post('/login/tokens')
def login(admin: AdminForLogin, session: Session = Depends(get_session)):
    admin = Admin.search_by_username(session=session, username=admin.username)
    if admin is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Username not found'
        )

    if verify_password(password=admin.password, hashed_password=admin.password) is False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Password is not correct'
        )

    admin_dict = admin.__dict__
    admin_dict.pop('passowrd')
    body = jsonable_encoder(admin_dict)

    token = make_token(id_=admin.id, role=Role.admin, username=admin.username, expire_delta=timedelta(seconds=20))
    header = {'token': token}

    return JSONResponse(content=body, headers=header)


@router.get('', response_model=List[AdminForRead])
def show_all(super_admin_token: Annotated[str, Header()], session: Session = Depends(get_session)):
    token_payload = check_token(super_admin_token)

    token_role = token_payload['role']
    if token_role != Role.super_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to see admin'
        )

    admins = Admin.show_all(session=session)

    return admins


@router.get('/{admin_id}', response_model=AdminForRead)
def show_specific(super_admin_token: Annotated[str, Header()], admin_id: str, session: Session = Depends(get_session)):
    token_payload = check_token(super_admin_token)

    token_role = token_payload['role']
    if token_role != Role.super_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to see admin'
        )

    admin = Admin.search_by_id(session=session, admin_id=admin_id)
    if admin is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='An admin with this id not found'
        )

    return admin


@router.delete('/{admin_id}', response_model=AdminForRead)
def delete(super_admin_token: Annotated[str, Header()], admin_id: int, session: Session = Depends(get_session)):
    token_payload = check_token(super_admin_token)

    token_role = token_payload['role']
    if token_role != Role.super_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You don\'t have access to delete admin'
        )

    deleted_admin = Admin.delete(session=session, admin_id=admin_id)

    return deleted_admin

