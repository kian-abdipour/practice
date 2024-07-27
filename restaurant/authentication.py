from jwt import encode, decode, InvalidTokenError, ExpiredSignatureError

from datetime import datetime, timedelta

from dotenv import load_dotenv
from os import getenv

from fastapi import HTTPException, status

import hashlib

from re import search

load_dotenv()
secret_key = getenv('SECRET_KEY')
algorithm_encrypt = getenv('ALGORYTHM_ENCRYPT')
algorithm_hash = getenv('ALGORYTHM_HASH')


def make_token(id_: int, username: str, expire_delta: timedelta):
    token_expire = datetime.utcnow().replace(microsecond=0) + expire_delta
    data = {
        'id': id_,
        'access_key': username,
        'exp': token_expire
    }

    jwt_access_token = encode(data, secret_key, algorithm=algorithm_encrypt)
    print(jwt_access_token)
    return jwt_access_token


def check_token(token: str):
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

    return payload


def get_hash_password(password):
    return getattr(hashlib, f'{algorithm_hash}')(password.encode()).hexdigest()


def verify_password(password, hashed_password):
    return getattr(hashlib, f'{algorithm_hash}')(password.encode()).hexdigest() == hashed_password


def verify_password_pattern(password):
    if len(password) != 8:
        return 'Len of your password should be 8'

    if search('[a-z]', password) and search('[A-z]', password) and\
            search('[0-9]', password) and search('[!@#$%]', password):
        return True

    else:
        return 'Password should contain a-z, A-Z, 0-9 and at least one of !@#$%'

