from fastapi import APIRouter, HTTPException, status, Depends, Header
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from restaurant.scheme.super_admin import SuperAdminForLogin, SuperAdminForAddition, SuperAdminForRead
from restaurant.database import get_session
from restaurant.model import SuperAdmin
from restaurant.authentication import verify_password, make_token, check_token, get_hash_password
from restaurant.model.helper import Role

from sqlalchemy.orm import Session

from datetime import timedelta

from typing import Annotated, List

from dotenv import load_dotenv
from os import getenv

load_dotenv()
top_level_super_admin_username = getenv('TOP_LEVEL_SUPER_ADMIN_USERNAME')

router = APIRouter(
    prefix='/super_admins',
    tags=['super_admin']
)


@router.post('/login/tokens')
def login(super_admin: SuperAdminForLogin, session: Session = Depends(get_session)):
    super_admin_in_database = SuperAdmin.search_by_username(session=session, username=super_admin.username)
    if super_admin_in_database is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Username not found'
        )

    if verify_password(password=super_admin.password, hashed_password=super_admin_in_database.password) is False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Password is not correct'
        )

    super_admin_dict = super_admin_in_database.__dict__
    super_admin_dict.pop('password')
    body = jsonable_encoder(super_admin_dict)

    token = make_token(
        id_=super_admin_in_database.id,
        role=Role.super_admin,
        username=super_admin_in_database.username,
        expire_delta=timedelta(hours=1)
    )
    header = {'token': token}

    return JSONResponse(content=body, headers=header)


@router.post('')
def addition(
        top_level_super_admin_token: Annotated[str, Header()],
        super_admin: SuperAdminForAddition,
        session: Session = Depends(get_session)
):
    token_payload = check_token(token=top_level_super_admin_token)

    username = token_payload['username']
    token_role = token_payload['role']
    if username != top_level_super_admin_username or token_role != Role.super_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You do not have access to addition super_admin'
        )

    if SuperAdmin.search_by_username(session=session, username=super_admin.username) is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='This username already exist choose another one'
        )

    hashed_password = get_hash_password(super_admin.password)
    added_super_admin = SuperAdmin.add(
        session=session, first_name=super_admin.first_name,
        last_name=super_admin.last_name, username=super_admin.username,
        password=hashed_password
    )

    super_admin_dict = added_super_admin.__dict__
    super_admin_dict.pop('password')
    body = jsonable_encoder(super_admin_dict)

    return JSONResponse(content=body)


@router.get('', response_model=List[SuperAdminForRead])
def show_all(top_level_super_admin_token: Annotated[str, Header()], session: Session = Depends(get_session)):
    token_payload = check_token(token=top_level_super_admin_token)

    username = token_payload['username']
    token_role = token_payload['role']
    if username != top_level_super_admin_username or token_role != Role.super_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You do not have access to see super_admins'
        )

    super_admins = SuperAdmin.show_all(session=session)

    return super_admins


@router.get('/{super_admin_id}', response_model=SuperAdminForRead)
def show_specific(
        top_level_super_admin_token: Annotated[str, Header()],
        super_admin_id: int,
        session: Session = Depends(get_session)
):
    token_payload = check_token(token=top_level_super_admin_token)

    username = token_payload['username']
    token_role = token_payload['role']
    if username != top_level_super_admin_username or token_role != Role.super_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You do not have access to see super_admins'
        )

    super_admin = SuperAdmin.search_by_id(session=session, super_admin_id=super_admin_id)

    if super_admin is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='A super admin with this id not found'
        )

    return super_admin


@router.delete('/{super_admin_id}', response_model=SuperAdminForRead)
def delete(
        top_level_super_admin_token: Annotated[str, Header()],
        super_admin_id: int,
        session: Session = Depends(get_session)
):
    token_payload = check_token(token=top_level_super_admin_token)

    username = token_payload['username']
    token_role = token_payload['role']
    if username != top_level_super_admin_username or token_role != Role.super_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You do not have access to delete super_admin'
        )

    deleted_super_admin = SuperAdmin.delete(session=session, super_admin_id=super_admin_id)
    if deleted_super_admin is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='a super admin with this id not found'
        )

    return deleted_super_admin

