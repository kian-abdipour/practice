from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from restaurant.scheme.super_admin import SuperAdminForLogin
from restaurant.database import get_session
from restaurant.model import SuperAdmin
from restaurant.authentication import verify_password, make_token
from restaurant.model.helper import Role

from sqlalchemy.orm import Session

from datetime import timedelta

from dotenv import load_dotenv
from os import getenv

load_dotenv()
top_level_super_admin_username = getenv('TOP_LEVEL_SUPER_ADMIN_USERNAME')

router = APIRouter(
    prefix='/super-admin',
    tags=['super_admin']
)


@router.post('-tokens')
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
        expire_delta=timedelta(days=365)
    )
    header = {'token': token}

    return JSONResponse(content=body, headers=header)

