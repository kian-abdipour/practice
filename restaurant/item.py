import sqlalchemy as sa
from sqlalchemy import *
from sqlalchemy.orm import relationship
from base import Base


class Item(Base):
    __tablename__ = 'items'
    item_id = Column('item', sa.INTEGER, primary_key=True, nullable=False, unique=True)
    name = Column('name', sa.VARCHAR(40))
    price = Column('price', sa.INTEGER)
    category_id = Column('category_id', sa.INTEGER, sa.ForeignKey('categories.category_id'))
    order = relationship('orders.order_id')

