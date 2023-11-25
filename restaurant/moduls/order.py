from sqlalchemy import Unicode, Column, Integer, ForeignKey, DateTime
from restaurant.moduls.base import Base
from sqlalchemy.orm import relationship
from datetime import datetime


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    state = Column(Unicode)
    desk_number = Column(Integer, nullable=True)
    unit_amount = Column(Integer, default=0)
    description = Column(Unicode, nullable=True)
    customer_id = Column(ForeignKey('customer.id'))

    items = relationship('OrderItem')
    payments = relationship('Payment')

