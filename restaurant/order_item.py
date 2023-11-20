from sqlalchemy import Column, Integer, ForeignKey
from base import Base
from sqlalchemy.orm import relationship


class OrderItem(Base):
    __tablename__ = 'orderitem'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    item_id = Column(Integer, ForeignKey('item.id'))
    quantity = Column(Integer, nullable=False)

    orders = relationship('Order')
    items = relationship('Item')

