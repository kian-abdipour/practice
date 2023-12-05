from sqlalchemy import Column, Integer, ForeignKey
from restaurant.moduls.base import Base
from sqlalchemy.orm import relationship
from restaurant.moduls.mixing_modul import Moment


class CategoryItem(Base, Moment):
    __tablename__ = 'category_item'
    id = Column(Integer, primary_key=True)
    category_id = Column(ForeignKey('category.id'))
    item_id = Column(ForeignKey('item.id'))

    categories = relationship('Category')
    items = relationship('Item')

