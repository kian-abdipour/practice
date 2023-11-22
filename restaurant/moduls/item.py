from sqlalchemy import Column, Integer, Unicode, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from restaurant.moduls.base import Base
from datetime import datetime


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(40), nullable=False)
    price = Column(Integer, nullable=False)
    condition_stock = Column(Boolean, nullable=False)
    description = Column(Unicode)
    category_id = Column(Integer, ForeignKey('category.id'))
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    orders = relationship('OrderItem')

