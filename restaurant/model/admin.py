from sqlalchemy import Column, Integer, Unicode, ForeignKey
from sqlalchemy.orm import Session, relationship

from restaurant.model.base import Base
from restaurant.model.mixin import DateTimeMixin
from restaurant.custom_exception import LengthError


class Admin(DateTimeMixin, Base):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode(40), nullable=False)
    last_name = Column(Unicode(40), nullable=False)
    username = Column(Unicode(16), unique=True, nullable=False)
    password = Column(Unicode(64), nullable=False)
    superadmin_id = Column(ForeignKey('super_admin.id'))

    super_admin = relationship('SuperAdmin', back_populates='admins')

    @classmethod
    def add(cls, session: Session, first_name, last_name, username, password, super_admin_id):
        admin = cls(
            first_name=first_name, last_name=last_name, username=username,
            password=password, superadmin_id=super_admin_id
        )
        session.add(admin)

        session.commit()
        session.refresh(admin)

        return admin

    @classmethod
    def delete(cls, session: Session, admin_id):
        admin = session.query(cls).filter(cls.id == admin_id).one_or_none()
        if admin is None:
            return None

        result = session.query(cls).filter(cls.id == admin_id).delete()
        session.commit()

        if result == 1:
            return admin

    @classmethod
    def search_by_id(cls, session: Session, admin_id):
        admin = session.query(cls).filter(cls.id == admin_id).one_or_none()

        return admin

    @classmethod
    def search_by_username(cls, session: Session, username):
        admin = session.query(cls).filter(cls.username == username).one_or_none()

        return admin

    @classmethod
    def show_all(cls, session: Session):
        admins = session.query(cls).all()

        return admins

