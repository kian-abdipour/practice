from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship
from base import Base


class Customer(Base):
    __tablename__ = 'customer'
    customer_id = Column('customer_id', Integer, primary_key=True, nullable=False, unique=True)
    username = Column('username', VARCHAR(40))
    password = Column('password', VARCHAR(40))
    item = relationship('Order', back_populates="item")

