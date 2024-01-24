from sqlalchemy import Column, Integer, Unicode, ForeignKey
from sqlalchemy.orm import relationship
from restaurant.modul.base import Base
from restaurant.modul.mixin import DateTimeMixin
from restaurant.modul.custom_exception import LengthError
from restaurant.database_package import Session


class Item(DateTimeMixin, Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(40), nullable=False, unique=True)
    country = Column(Unicode(30))
    price = Column(Integer, nullable=False)
    stock = Column(Integer, default=0, nullable=False)
    description = Column(Unicode)

    orders = relationship('OrderItem', cascade='all, delete')
    categories = relationship('CategoryItem', cascade='all, delete')

    @staticmethod
    def add():
        try:
            print('Enter name of Item')
            name = input(': ')
            if len(name) > 40:
                error = LengthError(massage='LengthError: Len of name is out of 40')
                raise error

            with Session() as session:
                result = session.query(Item).filter(Item.name == name).one_or_none()

            if result is not None:
                return print('Waring: This item name already exist try again')

            print('Enter country of Item')
            country = input(': ')
            if len(country) > 30:
                error = LengthError(massage='LengthError: Len of country is out of 30')
                raise error

        except LengthError:
            error.show_massage()

        try:
            print('Enter price of item, it must be just number and by dollar')  # Ask question
            price = int(input(': '))

        except ValueError:
            return print('ValueError: You should type just number')

        print('Enter stock of item it must be just number')  # Ask question
        try:
            stock = int(input(': '))

        except ValueError:
            return print('ValueError: your stock should be just number')

        print('If you need a description for this item enter it, else just type No')
        description = input(': ')
        if description == 'No' or description == 'no' or description == '':
            description = None

        item = Item(name=name, country=country, price=price, stock=stock, description=description)
        with Session() as session:
            session.add(item)

            session.commit()

            result = session.query(Item).filter(Item.name == name).one()
            print('Item successfully added')

        return result.id

