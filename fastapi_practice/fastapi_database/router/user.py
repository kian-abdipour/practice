from fastapi import HTTPException, status, Header, Depends, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

from fastapi_practice.fastapi_database.model.user import User
from fastapi_practice.fastapi_database.scheme.user import UserForLogin, UserForRead
from fastapi_practice.fastapi_database.database import get_session
from fastapi_practice.fastapi_database.authentication import make_token, check_token
from fastapi_practice.fastapi_database.authentication import get_hash_password, verify_password, verify_password_pattern

from typing import Any

from datetime import timedelta

from typing import Annotated


router = APIRouter(
    prefix='/users',
    tags=['user'],

)


@router.post('/signup')
def signup(session: Session = Depends(get_session), user: UserForLogin = Any) -> Any:
    result = User.search_by_username(session, user.username)
    if result is not False:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='This username already exist choose another one'
        )

    user.password = get_hash_password(user.password)
    user_created = User.create(session, user)
    token = make_token(username=user.username, expire_delta=timedelta(seconds=60))
    headers = {'token': token}
    user_dict = user_created.__dict__
    user_dict.pop('password')
    body = jsonable_encoder(user_dict)
    response = JSONResponse(headers=headers, content=body)

    return response


@router.get('', response_model=list[UserForRead])
def read_all(session: Session = Depends(get_session)):
    return User.get_all(session)


@router.get('/{user-id}', response_model=UserForRead)
def read_specific_by_id(session: Session = Depends(get_session), user_id: int = None):
    result = User.search_by_id(session, user_id)

    if result is not False:
        return result

    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found'
        )


@router.post('/tokens')
def login(session: Session = Depends(get_session), user: UserForLogin = None):
    result = User.search_by_username(session, user.username)
    if result is False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Username is not correct'
        )

    if verify_password(user.password, result.password) is False:
        raise HTTPException(
           status_code=status.HTTP_401_UNAUTHORIZED,
           detail='Password is not correct'
        )

    token = make_token(username=user.username, expire_delta=timedelta(seconds=60))
    headers = {'token': token}
    user_dict = result.__dict__
    user_dict.pop('password')
    body = jsonable_encoder(user_dict)
    response = JSONResponse(headers=headers, content=body)

    return response


@router.get('/me', response_model=UserForRead)
def read_current(session: Session = Depends(get_session), token: Annotated[str, Header()] = None):
    username = check_token(token)
    current_user = User.search_by_username(session, username)

    return current_user


@router.delete('/{user_id}/deletion', response_model=UserForRead)
def delete(session: Session = Depends(get_session), user_id: int = None):
    result = User.delete(session, user_id=user_id)
    if result is not False:
        return result

    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User with this id not found'
        )

