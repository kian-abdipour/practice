from datetime import datetime, timedelta

from typing import Annotated

from fastapi import FastAPI, HTTPException, status, Header
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from jwt import encode, decode, InvalidTokenError, ExpiredSignatureError

from user import User, UserForAuthentication
from user_database import user_database

from dotenv import load_dotenv
from os import getenv

load_dotenv()
secret_key = getenv('SECRET_KEY')
algorithm_encrypt = getenv('ALGORYTHM_ENCRYPT')

app = FastAPI()


def get_user(username):
    if username in user_database:
        user_dict = user_database[username]
        user = User(**user_dict)
        return user


def authenticate_user(username, password):
    user = get_user(username)
    if not user:
        return False

    if user.password != password:
        return False
    return user


def create_access_token(data: dict, expire_delta: timedelta):
    token_expire = datetime.utcnow().replace(microsecond=0) + expire_delta
    data.update({'exp': token_expire})
    jwt_access_token = encode(data, secret_key, algorithm=algorithm_encrypt)
    return jwt_access_token


def make_token(username):
    access_token_expire_delta = timedelta(seconds=60)
    access_token = create_access_token(data={'access_key': username}, expire_delta=access_token_expire_delta)
    return access_token


def check_token(token):
    try:
        payload = decode(token, secret_key, algorithm_encrypt)
        username = payload['access_key']
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Authentication failed token not found',

            )

    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Authentication failed token is expired'
        )

    except InvalidTokenError:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Authentication failed token not found',

            )

    return username


@app.post('/tokens')
def login(user_information: UserForAuthentication):
    user = authenticate_user(user_information.username, user_information.password)
    if user is False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',

        )

    if user.is_valid is False:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Authentication was successful but you can\'t access now',

        )

    token = make_token(user.username)
    header = {'token': token}
    body = jsonable_encoder({})
    response = JSONResponse(content=body, headers=header)
    return response


@app.get('/users/me')
def get_current_user(token: Annotated[str, Header()]):
    username = check_token(token)
    user = user_database[username]

    return user

