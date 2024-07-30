from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, Session

from restaurant.model.base import Base
from restaurant.model.mixin import DateTimeMixin
from restaurant.model import Category, Item
from restaurant.custom_exception import LengthError


class CategoryItem(DateTimeMixin, Base):
    __tablename__ = 'category_item'
    id = Column(Integer, primary_key=True)
    category_id = Column(ForeignKey('category.id'))
    item_id = Column(ForeignKey('item.id'))

    category = relationship('Category', overlaps='items', cascade='all, delete', back_populates='items')
    item = relationship('Item', overlaps='categories', cascade='all, delete', back_populates='categories')

    @classmethod
    def add(cls, session: Session, category_id, item_id):
        category_item = cls(category_id=category_id, item_id=item_id)

        # This part is for check that an item is already in this category  if it is return None
        result = session.query(cls).filter(cls.category_id == category_id, cls.item_id == item_id).all()
        if len(result) > 0:
            return None

        session.add(category_item)

        session.commit()
        session.refresh(category_item)

        return category_item

    @classmethod
    def delete(cls, session: Session, category_id, item_id):
        category_item = session.query(cls).filter(cls.category_id == category_id, cls.item_id == item_id).one_or_none()
        if category_item is None:
            return None

        session.query(cls).filter(cls.category_id == category_id, cls.item_id == item_id).delete()

        session.commit()

        return category_item

    @classmethod
    def show_item_side(cls, session: Session, category_id):
        results = session.query(Item).join(cls).filter(cls.category_id == category_id).all()

        return results

