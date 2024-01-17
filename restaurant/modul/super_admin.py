from sqlalchemy import Column, Integer, Unicode
from sqlalchemy.orm import relationship, query
from restaurant.modul.base import Base
from restaurant.modul.mixin import DateTimeMixin
from restaurant.database_package import Session


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
        print('Enter super admin first name')
        first_name = input(': ')
        if len(first_name) > 40:
            return print('Warning: Len first name is out of range!, try again')

        print('Enter super admin last name')
        last_name = input(': ')
        if len(last_name) > 40:
            return print('Warning: Len last name is out of range!, try again')

        print('Enter super admin username maximum len 16 characters')
        username = input(': ')
        if len(username) > 16:
            return print('Warning: Len username is out of range!, try again')

        print('Enter super admin password maximum len 8 characters')
        password = input(': ')
        if len(password) > 8:
            return print('Warning: Len password is out of range!, try again')

        # Adding process
        super_admin = SuperAdmin(first_name=first_name, last_name=last_name, username=username, password=password)
        with Session() as session:
            session.add(super_admin)

            session.commit()

        print(f'{username} successfully added to super admins')

    @staticmethod
    def delete():
        # Get data and make type safing
        print('Enter super admin username that you want to remove at least 16 character')
        username = input(': ')
        if len(username) > 16:
            return print('Warning: Len username is out of range!, try again')

        # Deleting proces
        with Session() as session:
            result = session.query(SuperAdmin).filter(SuperAdmin.username == username).delete()

            session.commit()

        if result == 1:
            print(f'{username} successfully deleted from super admins')

        else:
            print(f'{username} not found')

    @staticmethod
    def login():
        # Get data and make type safing
        print('Enter your username')
        username = input(': ')
        if len(username) > 16:
            return print('Warning: Len username is out of range!, try again')

        print('Enter your password')
        password = input(': ')
        if len(password) > 8:
            return print('Warning: Len password is out of range!, try again')

        with (Session() as session):
            result = session.query(SuperAdmin).filter(SuperAdmin.username == username, SuperAdmin.password == password
                                                      ).one_or_none()

        if result is None:
            print('Username or password not found, try again')
            return False, result

        else:
            print(f'Login was successful,{username} welcome to your super admin account')
            return True, result

