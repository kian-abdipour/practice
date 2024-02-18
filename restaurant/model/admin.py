from sqlalchemy import Column, Integer, Unicode, ForeignKey
from restaurant.model.base import Base
from restaurant.model.mixin import DateTimeMixin
from restaurant.custom_exception import LengthError
from restaurant.database import Session


class Admin(DateTimeMixin, Base):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode(30), nullable=False)
    last_name = Column(Unicode(30), nullable=False)
    username = Column(Unicode(16), unique=True, nullable=False)
    password = Column(Unicode(8), nullable=False)
    superadmin_id = Column(ForeignKey('super_admin.id'))

    @classmethod
    def add(cls, super_admin_id):
        try:
            print('Enter admin first name')
            first_name = input(': ')
            if len(first_name) > 30:
                error = LengthError(massage='LengthError: Len of first name is out of 40!, try again')
                raise error

            print('Enter admin last name')
            last_name = input(': ')
            if len(last_name) > 30:
                error = LengthError(massage='LengthError: Len of last name is out of 40!, try again')
                raise error

            print('Enter admin username maximum len 16 characters')
            username = input(': ')
            if len(username) > 16:
                error = LengthError(massage='LengthError: Len of username is out of 16!, try again')
                raise error

            with Session() as session:
                result = session.query(cls).filter(cls.username == username).one_or_none()

            if result is not None:
                return print('This username already exist try again')

            print('Enter admin password maximum len 8 characters')
            password = input(': ')
            if len(password) != 8:
                error = LengthError(massage='LengthError: Len of password should be (8), try again')
                raise error

        except LengthError:
            error.show_massage()
            return False

        # Adding process
        admin = cls(first_name=first_name, last_name=last_name, username=username,
                    password=password, superadmin_id=super_admin_id)
        with Session() as session:
            session.add(admin)

            session.commit()

        return True

    @classmethod
    def delete(cls):
        # Get data and make type safing
        try:
            print('Enter admin username that you want to remove at least 16 character')
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

        with Session() as session:
            result = session.query(cls).filter(cls.username == username, cls.password == password).one_or_none()

        if result is None:
            print('Username or password not found, try again')
            return False, result

        else:
            print(f'Login was successful,{username} welcome to your admin account')
            return True, result

    @classmethod
    def show_admin(cls):
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
                    for admin in result:
                        print(f'id: {admin.id}, created at: {admin.created_at}'
                              f' first name: {admin.first_name}, last name: {admin.last_name},'
                              f' username: {admin.username}, password: {admin.password},'
                              f' super_admin_id: {admin.superadmin_id}')

                else:
                    print('Now we don\'t have any admin')

            elif operation == 2:
                print('Enter username of admin that you want to see')
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
                          f' username: {result.username}, password: {result.password},'
                          f' super_admin_id: {result.superadmin_id}')

                else:
                    print('This username not found')

            elif operation == 3:
                proceed = False

            else:
                print('Number not found')

