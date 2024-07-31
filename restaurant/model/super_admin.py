from sqlalchemy import Column, Integer, Unicode
from sqlalchemy.orm import relationship, Session

from restaurant.model.base import Base
from restaurant.model.mixin import DateTimeMixin
from restaurant.custom_exception import LengthError


class SuperAdmin(DateTimeMixin, Base):
    __tablename__ = 'super_admin'
    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode(40), nullable=False)
    last_name = Column(Unicode(40), nullable=False)
    username = Column(Unicode(16), unique=True, nullable=False)
    password = Column(Unicode(64), nullable=False)

    admins = relationship('Admin', back_populates='super_admin')

    @classmethod
    def add(cls, session: Session, first_name, last_name, username, password):
        super_admin = cls(first_name=first_name, last_name=last_name, username=username, password=password)
        session.add(super_admin)
        session.commit()
        session.refresh(super_admin)

        return super_admin

    @classmethod
    def delete(cls, session: Session, super_admin_id):
        super_admin = cls.search_by_id(session=session, super_admin_id=super_admin_id)
        if super_admin is None:
            return None

        result = session.query(cls).filter(cls.id == super_admin_id).delete()

        session.commit()

        if result == 1:
            return super_admin

    @classmethod
    def search_by_username(cls, session: Session, username):
        result = session.query(cls).filter(cls.username == username).one_or_none()

        return result

    @classmethod
    def search_by_id(cls, session: Session, super_admin_id):
        result = session.query(cls).filter(cls.id == super_admin_id).one_or_none()

        return result

    @classmethod
    def show_all(cls, session: Session):
        result = session.query(cls).all()

        return result

