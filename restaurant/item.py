from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


class Item(Base):
    __tablename__ = 'item'
    item_id = Column('item_id', Integer, primary_key=True, nullable=False, unique=True)
    name = Column('name', VARCHAR(40))
    price = Column('price', Integer)
    category_id = Column("category_id", Integer, ForeignKey('category.category_id'))
    customer = relationship('Order', back_populates="customer")

