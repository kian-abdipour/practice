from sqlalchemy import Column, Integer, Unicode, DateTime
from sqlalchemy.orm import relationship
from restaurant.moduls.base import Base
from datetime import datetime


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    name = Column(Unicode(30))
    country = Column(Unicode(30), nullable=True)

    items = relationship('Item')

