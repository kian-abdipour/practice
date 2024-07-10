from fastapi import FastAPI, HTTPException, status, Header, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from dotenv import load_dotenv
from os import getenv

from sqlalchemy.orm import Session

from fastapi_practice.fastapi_database.model.user import User
from fastapi_practice.fastapi_database.scheme.user import UserForLogin, UserForRead
from fastapi_practice.fastapi_database.database import database_Session
from fastapi_practice.fastapi_database.token import make_token, check_token

from typing import Any

from datetime import timedelta

from typing import Annotated

load_dotenv()
secret_key = getenv('SECRET_KEY')
algorithm_encrypt = getenv('ALGORITHM_ENCRYPT')

app = FastAPI()


def get_session():
    database_session = database_Session()
    try:
        yield database_session

    finally:
        database_session.close()


@app.post('/user-creation', response_model=UserForRead)
def create_user(session: Session = Depends(get_session), user: UserForLogin = None) -> Any:
    result = User.search_by_username(session, user.username)
    if result is not False:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='This username already exist choose another one'
        )

    return User.create(session, user)


@app.get('/Users', response_model=list[UserForRead])
def read_all_users(session: Session = Depends(get_session)):
    return User.get_all(session)


@app.get('/Users/{user-id}', response_model=UserForRead)
def read_specific_user_by_id(session: Session = Depends(get_session), user_id: int = None):
    result = User.search_by_id(session, user_id)

    if result is not False:
        return result

    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found'
        )


@app.post('/tokens')
def login(session: Session = Depends(get_session), user: UserForLogin = None):
    result = User.search_by_username_password(session, user)
    if result is False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Username or password is not correct'
        )

    token = make_token(username=user.username, expire_delta=timedelta(seconds=60))
    headers = {'token': token}
    body = jsonable_encoder(result.__dict__)
    response = JSONResponse(headers=headers, content=body)

    return response


@app.get('/users/me')
def read_current_user(session: Session = Depends(get_session), token: Annotated[str, Header()] = None):
    username = check_token(token)
    current_user = User.search_by_username(session, username)

    return current_user


@app.delete('/users/{user_id}/deletion')
def delete_user(session: Session = Depends(get_session), user_id: int = None):
    result = User.delete(session, user_id=user_id)
    if result is True:
        return {'massage': 'User successfully deleted'}

    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User with this id not found'
        )

