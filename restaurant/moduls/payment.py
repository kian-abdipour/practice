from sqlalchemy import Column, Integer, Unicode, ForeignKey
from restaurant.moduls.base import Base
from restaurant.moduls.mixing_modul import Moment


class Payment(Base, Moment):
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True)
    state = Column(Unicode)
    type = Column(Unicode)
    amount = Column(Integer)
    order_id = Column(ForeignKey('order.id'))

