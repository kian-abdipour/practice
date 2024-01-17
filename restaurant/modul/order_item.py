from sqlalchemy import Column, Integer, ForeignKey
from restaurant.modul.base import Base
from sqlalchemy.orm import relationship
from restaurant.modul.mixin import DateTimeMixin


class OrderItem(Base, DateTimeMixin):
    __tablename__ = 'order_item'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, default=1, nullable=False)
    unit_amount = Column(Integer, nullable=False)
    total_amount = Column(Integer, default=0, nullable=False)
    order_id = Column(ForeignKey('order.id'))
    item_id = Column(ForeignKey('item.id'))

    orders = relationship('Order', overlaps='items', cascade='all, delete')
    items = relationship('Item', overlaps='orders', cascade='all, delete')

