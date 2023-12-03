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
    description = Column(Unicode, nullable=True)
    address_id = Column(ForeignKey('address.id'))
    customer_id = Column(ForeignKey('customer.id'))

    items = relationship('OrderItem')
    payments = relationship('Payment')

