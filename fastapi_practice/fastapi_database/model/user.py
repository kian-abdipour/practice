from fastapi_practice.fastapi_database.model.mixin import DateTimeMixin
from fastapi_practice.fastapi_database.model.base import Base

from sqlalchemy import Column, Integer, Unicode
from sqlalchemy.orm import Session


class User(DateTimeMixin, Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(Unicode(16), unique=True, nullable=False)
    password = Column(Unicode(70), nullable=False)

    @classmethod
    def create(cls, session: Session, user):
        user_database = cls(username=user.username, password=user.password)
        session.add(user_database)
        session.commit()
        session.refresh(user_database)
        return user_database

    @classmethod
    def delete(cls, session: Session, user_id):
        result = session.query(cls).filter(cls.id == user_id).delete()

        if result == 1:
            session.commit()
            return True

        else:
            return False

    @classmethod
    def get_all(cls, session: Session):
        result = session.query(cls).all()
        return result

    @classmethod
    def search_by_id(cls, session: Session, user_id):
        resul = session.query(cls).filter(cls.id == user_id).one_or_none()

        if resul is not None:
            return resul

        else:
            return False

    @classmethod
    def search_by_username(cls, session: Session, username):
        resul = session.query(cls).filter(cls.username == username).one_or_none()

        if resul is not None:
            return resul

        else:
            return False

