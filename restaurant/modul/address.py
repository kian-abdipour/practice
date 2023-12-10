from sqlalchemy import Column, Unicode, ForeignKey, Integer
from restaurant.modul.base import Base
from sqlalchemy.orm import relationship
from restaurant.modul.mixin import DateTimeMixin


class Address(DateTimeMixin, Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    address = Column(Unicode(150))
    customer_id = Column(ForeignKey('customer.id'))

    orders = relationship('Order')

