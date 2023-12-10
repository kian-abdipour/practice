from sqlalchemy import Column, Integer, ForeignKey
from restaurant.modul.base import Base
from sqlalchemy.orm import relationship
from restaurant.modul.mixin import DateTimeMixin


class CategoryItem(DateTimeMixin, Base):
    __tablename__ = 'category_item'
    id = Column(Integer, primary_key=True)
    category_id = Column(ForeignKey('category.id'))
    item_id = Column(ForeignKey('item.id'))

    categories = relationship('Category')
    items = relationship('Item')

