from sqlalchemy import Column, Integer, Unicode, ForeignKey
from restaurant.modul.base import Base
from restaurant.modul.mixin import DateTimeMixin


class Payment(DateTimeMixin, Base):
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True)
    state = Column(Unicode, nullable=False)
    type = Column(Unicode, nullable=False)
    amount = Column(Integer, nullable=False)
    order_id = Column(ForeignKey('order.id'))
    customer_id = Column(ForeignKey('customer.id'))

