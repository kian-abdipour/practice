from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from restaurant.scheme.admin import AdminForAddition, AdminForLogin, AdminForRead
from restaurant.database import get_session
from restaurant.model import Admin
from restaurant.authentication import get_hash_password, verify_password, check_token, make_token

from sqlalchemy.orm import Session

from datetime import timedelta

router = APIRouter(
    prefix='/admins',
    tags=['admin']
)


@router.post('', response_model=AdminForRead)
def addition(super_admin_token: str, admin: AdminForAddition, session: Session = Depends(get_session)):
    super_admin_id = check_token(super_admin_token)

    admin = Admin.search_by_username(session=session, username=admin.username)
    if admin is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='This username already exist choose another one'
        )

    hashed_password = get_hash_password(admin.password)

    added_admin = Admin.add(session=session, first_name=admin.first_name,
                            last_name=admin.last_name, username=admin.username,
                            password=hashed_password, super_admin_id=super_admin_id)

    return added_admin


@router.post('/login/tokens')
def login(admin: AdminForLogin, session: Session):
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

    token = make_token(id_=admin.id, username=admin.username, expire_delta=timedelta(seconds=20))
    header = {'token': token}

    return JSONResponse(content=body, headers=header)


@router.get('', response_model=[AdminForRead])
def show_all(super_admin_token: str, session: Session):
    check_token(super_admin_token)

    admins = Admin.show_all(session=session)

    return admins


@router.get('/{admin_id}', response_model=AdminForRead)
def show_specific(super_admin_token: str, admin_id: str, session: Session = Depends(get_session)):
    check_token(super_admin_token)

    admin = Admin.search_by_id(session=session, admin_id=admin_id)
    if admin is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='An admin with this id not found'
        )

    return admin


@router.delete('/{admin_id}', response_model=AdminForRead)
def delete(super_admin_token: str, admin_id: int, session: Session = Depends(get_session)):
    check_token(token=super_admin_token)

    deleted_admin = Admin.delete(session=session, admin_id=admin_id)

    return deleted_admin

