from sqlalchemy import Column, Integer, Unicode, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(40))
    price = Column(Integer)
    category_id = Column(Integer, ForeignKey('category.id'))
    orders = relationship('OrderItem')

