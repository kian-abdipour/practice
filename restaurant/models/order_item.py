from sqlalchemy import Column, Integer, ForeignKey, DateTime
from base import Base
from sqlalchemy.orm import relationship
from datetime import datetime


class OrderItem(Base):
    __tablename__ = 'order_item'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    item_id = Column(Integer, ForeignKey('item.id'))
    quantity = Column(Integer, nullable=False)
    receipt = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    orders = relationship('Order')
    items = relationship('Item')

