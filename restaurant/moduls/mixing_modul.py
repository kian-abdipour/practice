from sqlalchemy import Column, DateTime, Integer
from datetime import datetime
from sqlalchemy.orm import as_declarative, declared_attr, mapped_column


class Moment:
    created_at = Column(DateTime, default=datetime.utcnow)


@as_declarative()
class Base:
    @declared_attr
    def __tablename__(cls):
        return cls.__tablename__.lower()

    created_at = mapped_column(DateTime, default=datetime.utcnow, sort_order=-1)

