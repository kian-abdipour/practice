from sqlalchemy import Unicode, Column, Integer, ForeignKey
from restaurant.moduls.base import Base
from sqlalchemy.orm import relationship
from restaurant.moduls.mixing_modul import Moment


class Order(Base, Moment):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    state = Column(Unicode)
    delivery_type = Column(Unicode)
    desk_number = Column(Integer, nullable=True)
    description = Column(Unicode, nullable=True)
    address_id = Column(ForeignKey('address.id'))
    customer_id = Column(ForeignKey('customer.id'))

    items = relationship('OrderItem')
    payments = relationship('Payment')

