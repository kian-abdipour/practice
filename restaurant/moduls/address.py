from sqlalchemy import Column, Unicode, ForeignKey, Integer
#from restaurant.moduls.base import Base
from sqlalchemy.orm import relationship
from restaurant.moduls.mixing_modul import Moment, Base


class Address(Base, Moment):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    address = Column(Unicode(150))
    customer_id = Column(ForeignKey('customer.id'))

    orders = relationship('Order')

