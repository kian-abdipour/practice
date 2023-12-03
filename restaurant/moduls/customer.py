from sqlalchemy import Column, Integer, Unicode, DateTime
from sqlalchemy.orm import relationship
from restaurant.moduls.base import Base
from datetime import datetime


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    username = Column(Unicode(40))
    password = Column(Unicode(8))
    phone_number = Column(Unicode(15))
    address = Column(Unicode(80))

    orders = relationship('Order')
    payments = relationship('Payment')

