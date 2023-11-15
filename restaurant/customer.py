from sqlalchemy import Column, Integer, Unicode
from sqlalchemy.orm import relationship
from base import Base


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    username = Column(Unicode(40))
    password = Column(Unicode(40))
    orders = relationship('Order')

