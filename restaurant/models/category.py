from sqlalchemy import Column, Integer, Unicode, DateTime
from sqlalchemy.orm import relationship
from base import Base
from datetime import datetime


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(30), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    items = relationship('Item')

