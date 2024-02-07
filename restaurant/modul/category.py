from sqlalchemy import Column, Integer, Unicode
from sqlalchemy.orm import relationship
from restaurant.modul.base import Base
from restaurant.modul.mixin import DateTimeMixin
from restaurant.database_package import Session
from restaurant.modul.custom_exception import LengthError


class Category(DateTimeMixin, Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(40), nullable=False, unique=True)

    items = relationship('CategoryItem', cascade='all, delete')

    @staticmethod
    def add():
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
            result = session.query(Category).filter(Category.name == name).one_or_none()

        if result is None:
            category = Category(name=name)
            with Session() as session:
                session.add(category)

                session.commit()

            print('Category successfully added')

        else:
            print('Waring: This category name already exist try again')

    @staticmethod
    def delete():
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
            result = session.query(Category).filter(Category.name == name).delete()

            session.commit()

        if result == 1:
            print('Category successfully deleted')
            return True

        else:
            print('Category not found')
            return False

    @staticmethod
    def show_all():
        with Session() as session:
            result = session.query(Category).all()

        if len(result) > 0:
            for category in result:
                print(f'id: {category.id}, name: {category.name}')

        else:
            print('Now we don\'t have any category')

    @staticmethod
    def search():
        print('Enter name of category')
        Category.show_all()
        name = input(': ')

        # Make type safing
        try:
            if len(name) > 40:
                error = LengthError(massage='LengthError: Len of Name is out of 30!, try again')
                raise error

        except LengthError:
            error.show_massage()

        with Session() as session:
            result = session.query(Category).filter(Category.name == name).one_or_none()

        if result is not None:
            print(f'id: {result.id}, name: {result.name}')
            return result, name

        elif name == 'q':
            pass

        else:
            print('Waring: Category not found')
            return False, name

