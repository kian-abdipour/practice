from sqlalchemy import Column, Integer, Unicode, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from restaurant.moduls.base import Base
from datetime import datetime


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    name = Column(Unicode(40))
    price = Column(Integer)
    stock = Column(Integer, default=0)
    description = Column(Unicode, nullable=True)
    category_id = Column(ForeignKey('category.id'))

    orders = relationship('OrderItem')

