from sqlalchemy import Column, DateTime
from datetime import datetime


class DateTimeMixin:
    created_at = Column(DateTime, default=datetime.utcnow)

