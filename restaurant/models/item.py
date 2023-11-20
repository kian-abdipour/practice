from sqlalchemy import Column, Integer, Unicode, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from base import Base
from datetime import datetime


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(40), nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(Unicode)
    category_id = Column(Integer, ForeignKey('category.id'))
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    orders = relationship('OrderItem')

