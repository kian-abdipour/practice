from sqlalchemy import Column, DateTime
from datetime import datetime
import hashlib


class DateTimeMixin:
    created_at = Column(DateTime, default=datetime.utcnow)


def get_hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password, hashed_password):
    return hashlib.sha256(password.encode()).hexdigest() == hashed_password

