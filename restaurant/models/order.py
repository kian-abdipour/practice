from sqlalchemy import Unicode, Column, Integer, ForeignKey, DateTime, Boolean
from base import Base
from sqlalchemy.orm import Relationship


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    desk_number = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)
    time = Column(DateTime, nullable=False)
    description = Column(Unicode)
    customer_id = Column(Integer, ForeignKey('customer.id'))

    items = Relationship('OrderItem')

