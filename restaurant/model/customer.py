from sqlalchemy import Column, Integer, Unicode
from sqlalchemy.orm import relationship
from restaurant.model.base import Base
from restaurant.model.mixin import DateTimeMixin
from restaurant.custom_exception import LengthError
#from restaurant.database import Session


class Customer(DateTimeMixin, Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    username = Column(Unicode(20), unique=True, nullable=False)
    password = Column(Unicode(8), nullable=False)
    phone_number = Column(Unicode(11), unique=True, nullable=False)

    orders = relationship('Order', cascade='all, delete')
    payments = relationship('Payment', cascade='all, delete')
    addresses = relationship('Address', cascade='all, delete')
    discounts = relationship('Discount', cascade='all, delete')

    @classmethod
    def signup(cls):
        # Make type safing
        try:
            print('Enter your username at least 20 character')
            username = input(': ')
            if len(username) > 20:
                error = LengthError(massage='LengthError: Len of username is out of 20!, try again')
                raise error

            with Session() as session:
                result = session.query(cls).filter(cls.username == username).one_or_none()

            if result is not None:
                print('Waring: This username has been taken before!, please choose another')
                return False, None

            print('Enter your password at least 8 character')
            password = input(': ')
            if len(password) != 8:
                error = LengthError(massage='LengthError: Len of password should be (8), try again')
                raise error

            print('Enter your phone number at least 11 and start with 09')
            phone_number = input(': ')
            if len(phone_number) != 11:
                error = LengthError(massage='LengthError: Len of phone number must be 11, try again')
                raise error

            elif phone_number[0] + phone_number[1] != '09':
                print('Waring: The phone number should start with 09 try again')
                return False, None

            with Session() as session:
                result = session.query(cls).filter(cls.phone_number == phone_number).one_or_none()

            if result is not None:
                print('Waring: This phone number already has an account!')
                return False, None

        except LengthError:
            error.show_massage()
            return False, None

        customer = cls(username=username, password=password, phone_number=phone_number)
        with Session() as session:
            session.add(customer)

            session.commit()

        print(f'Signup was successful, {username} welcome to your account')

        with Session() as session:
            result = session.query(cls).filter(cls.username == username).one()

        return True, result.id

    @classmethod
    def login(cls):
        # Make type safing
        try:
            print('Enter your username at least 20 character')
            username = input(': ')
            if len(username) > 20:
                error = LengthError(massage='LengthError: Len of username is out of 20!, try again')
                raise error

            print('Enter your password at least 8 character')
            password = input(': ')
            if len(password) != 8:
                error = LengthError(massage='LengthError: Len of password should be (8), try again')
                raise error

        except LengthError:
            error.show_massage()
            return False, None

        with Session() as session:
            result = session.query(cls).filter(cls.username == username, cls.password == password).one_or_none()

        if result is not None:
            print(f'Login was successful, welcome to your account {username}')
            return True, result.id

        else:
            print('Username or password not found try again')
            return False, None

