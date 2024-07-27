from sqlalchemy import Column, Integer, Unicode
from sqlalchemy.orm import relationship, Session

from restaurant.model.base import Base
from restaurant.model.mixin import DateTimeMixin


class Category(DateTimeMixin, Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(40), nullable=False, unique=True)

    items = relationship('CategoryItem', cascade='all, delete')

    @classmethod
    def add(cls, session: Session, name):
        category = cls(name=name)
        session.add(category)

        session.commit()
        session.refresh(category)

        return category

    @classmethod
    def delete(cls, session: Session, id_):
        category = session.query(cls).filter(cls.id == id_).one_or_none()
        if category is None:
            return None

        session.query(cls).filter(cls.id == id_).delete()

        session.commit()

        return category

    @classmethod
    def show_all(cls, session: Session):
        result = session.query(cls).all()

        return result

    @classmethod
    def search_by_name(cls, session: Session, name):
        result = session.query(cls).filter(cls.name == name).one_or_none()

        return result

    @classmethod
    def search_by_id(cls, session: Session, category_id):
        result = session.query(cls).filter(cls.id == category_id).one_or_none()

        return result

