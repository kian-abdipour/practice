from sqlalchemy import Column, Integer, Unicode
from sqlalchemy.orm import relationship, query
from restaurant.modul.base import Base
from restaurant.modul.mixin import DateTimeMixin
from restaurant.database_package import Session
from restaurant.modul.custom_exception import LengthError


class SuperAdmin(DateTimeMixin, Base):
    __tablename__ = 'super_admin'
    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode(40), nullable=False)
    last_name = Column(Unicode(40), nullable=False)
    username = Column(Unicode(16), unique=True, nullable=False)
    password = Column(Unicode(8), nullable=False)

    admins = relationship('Admin', cascade='all, delete')

    @staticmethod
    def add():
        # Get data and make type safing
        try:
            print('Enter super admin first name')
            first_name = input(': ')
            if len(first_name) > 40:
                error = LengthError(massage='LengthError: Len of first name is out of 40!, try again')
                raise error

            print('Enter super admin last name')
            last_name = input(': ')
            if len(last_name) > 40:
                error = LengthError(massage='LengthError: Len of last name is out of 40!, try again')
                raise error

            print('Enter super admin username maximum len 16 characters')
            username = input(': ')
            if len(username) > 16:
                error = LengthError(massage='LengthError: Len of username is out of 16!, try again')
                raise error

            print('Enter super admin password maximum len 8 characters')
            password = input(': ')
            if len(password) > 8:
                error = LengthError(massage='LengthError: Len of password is out of 8!, try again')
                raise error

        except LengthError:
            error.show_massage()
            return False

        # Adding process
        super_admin = SuperAdmin(first_name=first_name, last_name=last_name, username=username, password=password)
        with Session() as session:
            session.add(super_admin)

            session.commit()

        return True

    @staticmethod
    def delete():
        # Get data and make type safing
        try:
            print('Enter super admin username that you want to remove at least 16 character')
            username = input(': ')
            if len(username) > 16:
                error = LengthError('LengthError: Len of username is out of 16!, try again')
                raise error
        except LengthError:
            return False

        # Deleting proces
        with Session() as session:
            result = session.query(SuperAdmin).filter(SuperAdmin.username == username).delete()

            session.commit()

        if result == 1:
            return True

        else:
            print('Super admin not found')
            return False

    @staticmethod
    def login():
        # Get data and make type safing
        try:
            print('Enter your username')
            username = input(': ')
            if len(username) > 16:
                error = LengthError(massage='LengthError: Len of username is out of 16!, try again')
                raise error

            print('Enter your password')
            password = input(': ')
            if len(password) > 8:
                error = LengthError(massage='LengthError: Len of password is out of 8!, try again')
                raise error

        except LengthError:
            error.show_massage()
            return False, False

        with (Session() as session):
            result = session.query(SuperAdmin).filter(SuperAdmin.username == username, SuperAdmin.password == password
                                                      ).one_or_none()

        if result is None:
            print('Username or password not found, try again')
            return False, result

        else:
            print(f'Login was successful,{username} welcome to your super admin account')
            return True, result

