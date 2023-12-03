from sqlalchemy import Unicode, Column, Integer, ForeignKey, DateTime
from restaurant.moduls.base import Base
from sqlalchemy.orm import relationship
from datetime import datetime


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    state = Column(Unicode)
    delivery_type = Column(Unicode)
    desk_number = Column(Integer, nullable=True)
    address = Column(Unicode(80), nullable=True)
    description = Column(Unicode, nullable=True)
    customer_id = Column(ForeignKey('customer.id'))

    items = relationship('OrderItem')
    payments = relationship('Payment')

