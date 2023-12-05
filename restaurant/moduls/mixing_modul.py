from sqlalchemy import Column, DateTime
from datetime import datetime


class Moment:
    created_at = Column(DateTime, default=datetime.utcnow)

