import sqlalchemy as sa
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Order(Base):
    __tablename__ = 'orders'
    order_id = Column('order_id', sa.INTEGER, primary_key=True, nullable=False, unique=True)
    customer_id = Column('customer_id', sa.ForeignKey('customers.customer_id'))
    item_id = Column('item_id', sa.ForeignKey('item.item_id'))

