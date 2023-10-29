import sqlalchemy as sa
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'
    customer_id = Column('customer_id', sa.INTEGER, primary_key=True, nullable=False, unique=True)
    username = Column('username', sa.VARCHAR(40))
    password = Column('password', sa.VARCHAR(40))
    order = relationship('orders.order_id')

