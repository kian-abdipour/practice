from sqlalchemy import Column, Integer, Unicode
from sqlalchemy.orm import relationship
from restaurant.modul.base import Base
from restaurant.modul.mixin import DateTimeMixin


class Customer(DateTimeMixin, Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    username = Column(Unicode(40))
    password = Column(Unicode(8))
    phone_number = Column(Unicode(11), unique=True)

    orders = relationship('Order', cascade='all, delete')
    payments = relationship('Payment', cascade='all, delete')
    addresses = relationship('Address', cascade='all, delete')

