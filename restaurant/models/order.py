from sqlalchemy import Unicode, Column, Integer, ForeignKey, DateTime
from base import Base
from sqlalchemy.orm import Relationship
from datetime import datetime


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    desk_number = Column(Integer, nullable=False)
    description = Column(Unicode)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    items = Relationship('OrderItem')

