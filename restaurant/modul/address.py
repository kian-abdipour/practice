from sqlalchemy import Column, Unicode, ForeignKey, Integer
from restaurant.modul.base import Base
from sqlalchemy.orm import relationship
from restaurant.modul.mixin import DateTimeMixin
from restaurant.database_package import Session
from restaurant.modul.custom_exception import LengthError


class Address(DateTimeMixin, Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    address = Column(Unicode(150), nullable=False)
    customer_id = Column(ForeignKey('customer.id'))

    orders = relationship('Order', cascade='all, delete')

    @staticmethod
    def add(customer_id):
        print('Enter your address')
        try:
            text_address = input(': ')
            if len(text_address) > 150:
                error = LengthError(massage='LengthError: The address is very long')
                raise error

        except LengthError:
            error.show_massage()
            return False

        address = Address(address=text_address, customer_id=customer_id)
        with Session() as session:
            session.add(address)

            session.commit()

        print('Your address successfully added')
        return True

