from sqlalchemy import Column, Integer, Unicode, ForeignKey
from restaurant.modul.base import Base
from restaurant.modul.mixin import DateTimeMixin


class Payment(DateTimeMixin, Base):
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True)
    state = Column(Unicode)
    type = Column(Unicode)
    amount = Column(Integer)
    order_id = Column(ForeignKey('order.id'))

