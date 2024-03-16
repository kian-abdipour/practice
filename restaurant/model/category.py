from sqlalchemy import Column, Integer, Unicode
from sqlalchemy.orm import relationship

from restaurant.model.base import Base
from restaurant.model.mixin import DateTimeMixin
from restaurant.database import Session
from restaurant.custom_exception import LengthError


class Category(DateTimeMixin, Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(40), nullable=False, unique=True)

    items = relationship('CategoryItem', cascade='all, delete')

    @classmethod
    def add(cls):
        print('Enter name of your category')
        name = input(': ')

        # Make type safing
        try:
            if len(name) > 40:
                error = LengthError(massage='LengthError: Len of Name is out of 30!, try again')
                raise error

        except LengthError:
            error.show_massage()

        with Session() as session:
            result = session.query(cls).filter(cls.name == name).one_or_none()

        if result is None:
            category = cls(name=name)
            with Session() as session:
                session.add(category)

                session.commit()

            print('Category successfully added')

        else:
            print('Waring: This category with this name already exist try again')

    @classmethod
    def delete(cls):
        print('Enter name of category that you want to delete')
        name = input(': ')

        # Make type safing
        try:
            if len(name) > 40:
                error = LengthError(massage='LengthError: Len of Name is out of 30!, try again')
                raise error

        except LengthError:
            error.show_massage()

        with Session() as session:
            result = session.query(cls).filter(cls.name == name).delete()

            session.commit()

        if result == 1:
            print('Category successfully deleted')
            return True

        else:
            print('Category not found')
            return False

    @classmethod
    def show_all(cls):
        with Session() as session:
            result = session.query(cls).all()

        if len(result) > 0:
            for category in result:
                print(f'id: {category.id}, name: {category.name}')

        else:
            print('Now we don\'t have any category')
            return False

    @classmethod
    def search(cls):
        if cls.show_all() is not False:
            print('Enter name of category')
            name = input(': ')

            # Make type safing
            try:
                if len(name) > 40:
                    error = LengthError(massage='LengthError: Len of Name is out of 30!, try again')
                    raise error

            except LengthError:
                error.show_massage()

            with Session() as session:
                result = session.query(cls).filter(cls.name == name).one_or_none()

            if result is not None:
                print(f'id: {result.id}, name: {result.name}')
                return result, name

            elif name == 'q':
                return False, name

            else:
                print('Waring: Category not found')
                return False, name

        else:
            return False, 'q'

