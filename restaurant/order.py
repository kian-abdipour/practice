from sqlalchemy import Column, Integer, ForeignKey
from base import Base
from sqlalchemy.orm import relationship


class Order(Base):
    __tablename__ = 'order'
    order_id = Column('order_id', Integer, primary_key=True, nullable=False, unique=True)
    customer_id = Column('customer_id', Integer, ForeignKey('customer.customer_id'), primary_key=True)
    item_id = Column('item_id', Integer, ForeignKey('item.item_id'), primary_key=True)
    customer = relationship("Customer", back_populates="item")
    item = relationship("Item", back_populates="customer")

