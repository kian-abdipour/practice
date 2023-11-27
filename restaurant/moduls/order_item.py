from sqlalchemy import Column, Integer, ForeignKey, DateTime
from restaurant.moduls.base import Base
from sqlalchemy.orm import relationship
from datetime import datetime


class OrderItem(Base):
    __tablename__ = 'order_item'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    quantity = Column(Integer, default=1)
    total_amount = Column(Integer, default=0)
    order_id = Column(ForeignKey('order.id'))
    item_id = Column(ForeignKey('item.id'))

    orders = relationship('Order')
    items = relationship('Item')

