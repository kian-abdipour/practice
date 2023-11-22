from sqlalchemy import Column, Integer, Unicode, DateTime
from sqlalchemy.orm import relationship
from restaurant.moduls.base import Base
from datetime import datetime


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(30), nullable=False)
    country = Column(Unicode(20), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    items = relationship('Item')

