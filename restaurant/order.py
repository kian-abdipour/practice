from sqlalchemy import Column, Integer, ForeignKey
from base import Base
from sqlalchemy.orm import Relationship


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    items = Relationship('OrderItem')

