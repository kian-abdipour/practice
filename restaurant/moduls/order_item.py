from sqlalchemy import Column, Integer, ForeignKey
#from restaurant.moduls.base import Base
from sqlalchemy.orm import relationship
from restaurant.moduls.mixing_modul import Moment, Base


class OrderItem(Base, Moment):
    __tablename__ = 'order_item'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, default=1)
    unit_amount = Column(Integer)
    total_amount = Column(Integer, default=0)
    order_id = Column(ForeignKey('order.id'))
    item_id = Column(ForeignKey('item.id'))

    orders = relationship('Order')
    items = relationship('Item')

