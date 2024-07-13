from jwt import encode, decode, InvalidTokenError, ExpiredSignatureError

from datetime import datetime, timedelta

from dotenv import load_dotenv
from os import getenv

from fastapi import HTTPException, status


load_dotenv()
secret_key = getenv('SECRET_KEY')
algorithm_encrypt = getenv('ALGORYTHM_ENCRYPT')


def make_token(username: str, expire_delta: timedelta):
    token_expire = datetime.utcnow().replace(microsecond=0) + expire_delta
    data = {'access_key': username,
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

    return username

