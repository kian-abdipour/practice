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

    @staticmethod
    def show_all(customer_id):
        with Session() as session:
            result = session.query(Address).filter(Address.customer_id == customer_id).all()

        if len(result) > 0:
            for address in result:
                print(f'id: {address.id}, address: {address.address}')

        else:
            print('Now you don\' have any address')

    @staticmethod
    def delete(address_id, customer_id):
        with Session() as session:
            result = session.query(Address).filter(Address.id == address_id,
                                                   Address.customer_id == customer_id).delete()

            session.commit()

        if result == 1:
            print('Address successfully deleted')

        else:
            print('Waring: Address id not found, try again')

    @staticmethod
    def search(address_id, customer_id):
        with Session() as session:
            result = session.query(Address).filter(Address.id == address_id,
                                                   Address.customer_id == customer_id).one_or_none()

        if result is not None:
            return result.id

        else:
            print('Waring: Address id not found, try again')
            return False

