from sqlalchemy import Column, Integer, Unicode
from sqlalchemy.orm import relationship
#from restaurant.moduls.base import Base
from restaurant.moduls.mixing_modul import Moment, Base


class Customer(Base, Moment):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    username = Column(Unicode(40))
    password = Column(Unicode(8))
    phone_number = Column(Unicode(11), unique=True)

    orders = relationship('Order')
    payments = relationship('Payment')
    addresses = relationship('Address')

