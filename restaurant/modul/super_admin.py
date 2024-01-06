from sqlalchemy import Column, Integer, Unicode
from sqlalchemy.orm import relationship
from restaurant.modul.base import Base
from restaurant.modul.mixin import DateTimeMixin
from restaurant.database_package import Session


class SuperAdmin(DateTimeMixin, Base):
    __tablename__ = 'super_admin'
    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode(30))
    last_name = Column(Unicode(30))
    username = Column(Unicode(16))
    password = Column(Unicode(8))

    admins = relationship('Admin', cascade='all, delete')

    @staticmethod
    def add_super_admin():
        print('Enter super admin first name')
        first_name = input(': ')

        print('Enter super admin last name')
        last_name = input(': ')

        print('Enter super admin username maximum len 16 characters')
        username = input(': ')

        print('Enter super admin password maximum len 8 characters')
        password = input(': ')

        super_admin = SuperAdmin(first_name=first_name, last_name=last_name, username=username, password=password)
        with Session as session:
            session.add(super_admin)

            session.commit()

