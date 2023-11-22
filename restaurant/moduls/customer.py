from sqlalchemy import Column, Integer, Unicode, DateTime
from sqlalchemy.orm import relationship
from base import Base
from datetime import datetime


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    username = Column(Unicode(40), nullable=False)
    password = Column(Unicode(8), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    orders = relationship('Order')

