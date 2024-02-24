from sqlalchemy import Column, Integer, Unicode
from sqlalchemy.orm import relationship
from restaurant.model.base import Base
from restaurant.model.mixin import DateTimeMixin
#from restaurant.database import Session
from restaurant.custom_exception import LengthError


class SuperAdmin(DateTimeMixin, Base):
    __tablename__ = 'super_admin'
    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode(40), nullable=False)
    last_name = Column(Unicode(40), nullable=False)
    username = Column(Unicode(16), unique=True, nullable=False)
    password = Column(Unicode(8), nullable=False)

    admins = relationship('Admin', cascade='all, delete')

    @classmethod
    def add(cls):
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
            if len(password) != 8:
                error = LengthError(massage='LengthError: Len of password should be (8), try again')
                raise error

        except LengthError:
            error.show_massage()
            return False

        # Adding process
        super_admin = cls(first_name=first_name, last_name=last_name, username=username, password=password)
        with Session() as session:
            session.add(super_admin)

            session.commit()

        return True

    @classmethod
    def delete(cls):
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
            result = session.query(cls).filter(cls.username == username).delete()

            session.commit()

        if result == 1:
            return True

        else:
            print('Super admin not found')
            return False

    @classmethod
    def login(cls):
        # Get data and make type safing
        try:
            print('Enter your username')
            username = input(': ')
            if len(username) > 16:
                error = LengthError(massage='LengthError: Len of username is out of 16!, try again')
                raise error

            print('Enter your password')
            password = input(': ')
            if len(password) != 8:
                error = LengthError(massage='LengthError: Len of password should be (8), try again')
                raise error

        except LengthError:
            error.show_massage()
            return False, False

        with (Session() as session):
            result = session.query(cls).filter(cls.username == username, cls.password == password).one_or_none()

        if result is None:
            print('Username or password not found, try again')
            return False, result

        else:
            print(f'Login was successful,{username} welcome to your super admin account')
            return True, result

    @classmethod
    def show_super_admin(cls):
        proceed = True
        while proceed:
            print('Enter a number\n1.All\n2.Search\n3.back')
            try:
                operation = int(input(': '))

            except ValueError:
                print('ValueError: You should type just number try again')
                operation = None

            if operation == 1:
                with Session() as session:
                    result = session.query(cls).all()

                if len(result) > 0:
                    for super_admin in result:
                        print(f'id: {super_admin.id}, created at: {super_admin.created_at}'
                              f' first name: {super_admin.first_name}, last name: {super_admin.last_name},'
                              f' username: {super_admin.username}, password: {super_admin.password}')

                else:
                    print('Now we don\'t have any super admin')

            elif operation == 2:
                print('Enter username of super admin that you want to see')
                username = input(': ')

                try:
                    if len(username) > 16:
                        error = LengthError(massage='LengthError: Len of username is out of 16!, try again')
                        raise error

                except LengthError:
                    error.show_massage()

                with Session() as session:
                    result = session.query(cls).filter(cls.username == username).one_or_none()

                if result is not None:
                    print(f'id: {result.id}, created at: {result.created_at}'
                          f' first name: {result.first_name}, last name: {result.last_name},'
                          f' username: {result.username}, password: {result.password}')

                else:
                    print('This username not found')

            elif operation == 3:
                proceed = False

            else:
                print('Number not found')

