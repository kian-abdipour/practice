from sqlalchemy import Column, DateTime
from datetime import datetime
from passlib.context import CryptContext


class DateTimeMixin:
    created_at = Column(DateTime, default=datetime.utcnow)


password_crypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_hash_password(password):
    return password_crypt_context.hash(password)


def verify_password(password, hashed_password):
    return password_crypt_context.verify(password, hashed_password)

