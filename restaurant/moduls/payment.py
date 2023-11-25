from sqlalchemy import Column, Integer, Unicode, ForeignKey, DateTime, Boolean
from restaurant.moduls.base import Base
from datetime import datetime


class Payment(Base):
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    type = Column(Unicode)
    total_amount = Column(Integer)
    condition = Column(Boolean)
    order_id = Column(ForeignKey('order.id'))

