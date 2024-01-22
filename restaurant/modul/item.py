from sqlalchemy import Column, Integer, Unicode, ForeignKey
from sqlalchemy.orm import relationship
from restaurant.modul.base import Base
from restaurant.modul.mixin import DateTimeMixin


class Item(DateTimeMixin, Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(40), nullable=False, unique=True)
    country = Column(Unicode(30))
    price = Column(Integer, nullable=False)
    stock = Column(Integer, default=0, nullable=False)
    description = Column(Unicode)
    category_id = Column(ForeignKey('category.id'))

    orders = relationship('OrderItem', cascade='all, delete')
    categories = relationship('CategoryItem', cascade='all, delete')

