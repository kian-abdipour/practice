from sqlalchemy import Column, Unicode, ForeignKey, DateTime
from restaurant.moduls.base import Base
from datetime import datetime
from sqlalchemy.orm import relationship


class Address(Base):
    __tablename__ = 'address'
    created_at = Column(DateTime, default=datetime.utcnow)
    address = Column(Unicode(150))
    customer_id = Column(ForeignKey('customer.id'))

    orders = relationship('Order')
