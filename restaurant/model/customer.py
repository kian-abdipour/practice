from sqlalchemy import Column, Integer, Unicode, ForeignKey
from sqlalchemy.orm import relationship, Session
from restaurant.model.base import Base
from restaurant.model.mixin import DateTimeMixin
from restaurant.custom_exception import LengthError
#from restaurant.database import Session


class Customer(DateTimeMixin, Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    username = Column(Unicode(20), unique=True, nullable=False)
    password = Column(Unicode(64), nullable=False)
    phone_number = Column(Unicode(11), unique=True, nullable=False)

    orders = relationship('Order', back_populates='customer')
    payments = relationship('Payment', back_populates='customer')
    addresses = relationship('Address', back_populates='customer')
    cart = relationship('Cart', back_populates='customer', uselist=False)

    @classmethod
    def add(cls, session: Session, username, password, phone_number):
        customer = cls(username=username, password=password, phone_number=phone_number)
        session.add(customer)

        session.commit()
        session.refresh(customer)

        return customer

    @classmethod
    def search_by_username(cls, session: Session, username):
        result = session.query(cls).filter(cls.username == username).one_or_none()

        return result

    @classmethod
    def search_by_username_password(cls, session: Session, username, password):
        result = session.query(cls).filter(cls.username == username, cls.password == password).one_or_none()

        return result

    @classmethod
    def search_by_phone_number(cls, session: Session, phone_number):
        result = session.query(cls).filter(cls.phone_number == phone_number).one_or_none()

        return result

    @classmethod
    def show_all(cls, session: Session):
        customers = session.query(cls).all()

        return customers

    def __convert_to_dict__(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'phone_number': self.phone_number,
            'created_at': self.created_at
        }

