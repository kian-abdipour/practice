from sqlalchemy import Column, Integer, Unicode, Float
from sqlalchemy.orm import relationship, Session

from restaurant.model.base import Base
from restaurant.model.mixin import DateTimeMixin
from restaurant.custom_exception import OutOfStockError


class Item(DateTimeMixin, Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(40), nullable=False, unique=True)
    country = Column(Unicode(30))
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0, nullable=False)
    description = Column(Unicode)

    orders = relationship('OrderItem', back_populates='item')
    categories = relationship('CategoryItem', back_populates='item')
    carts = relationship('CartItem', back_populates='item')

    @classmethod
    def add(cls, session: Session, name, country, price, stock, description):
        item = cls(name=name, country=country, price=price, stock=stock, description=description)
        session.add(item)

        session.commit()
        session.refresh(item)

        return item

    @classmethod
    def show_all(cls, session: Session):
        result = session.query(cls).all()

        return result

    @classmethod
    def search_by_name(cls, session: Session, name):
        result = session.query(cls).filter(cls.name == name).one_or_none()

        return result

    @classmethod
    def search_by_id(cls, session: Session, item_id):
        result = session.query(cls).filter(cls.id == item_id).one_or_none()

        return result

    @classmethod
    def addition_to_stock(cls, item):
        print(f'Enter a number that you want to addition to stock of {item.name}')
        try:
            addition_stock = int(input(': '))

        except ValueError:
            return print('ValueError: You should type just number, try again')

        if addition_stock <= 0:
            return print('Waring: The number should be bigger than zero')

        with Session() as session:
            session.query(cls).filter(cls.id == item.id).update({cls.stock: (cls.stock + addition_stock)})

            session.commit()

        print(f'Addition to stock was successful, now the stock of {item.name} is {item.stock + addition_stock}')

    @classmethod
    def check_item_stock(cls, item, quantity):
        if quantity > item.stock:
            raise OutOfStockError(massage=f'Stock of {item.name} with id {item.id} is {item.stock} and you want {quantity}')

