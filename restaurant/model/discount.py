import random
import re
import string
from datetime import date

from sqlalchemy import Column, Integer, Unicode, String, Float, Date
from sqlalchemy.orm import relationship

from restaurant.custom_exception import LengthError
from restaurant.database import Session
from restaurant.model.base import Base
from restaurant.model.helper import character_for_discount_code
from restaurant.model.mixin import DateTimeMixin


class Discount(DateTimeMixin, Base):
    __tablename__ = 'discount'
    id = Column(Integer, primary_key=True)
    start_date = Column(Date)
    expire_date = Column(Date)
    title = Column(Unicode(40), nullable=False)
    percent = Column(Float, nullable=False)
    code = Column(String(10), nullable=False)
    description = Column(Unicode)
    usage_limitation = Column(Integer)

    discount_histories = relationship('DiscountHistory', cascade='all, delete')

    @classmethod
    def add(cls, code):
        try:
            print('Enter title of your discount')
            title = input(': ')
            if len(title) > 40:
                error = LengthError(massage='LengthError: Title is too long! try again')
                raise error

            print('Enter percent of your discount is should be 1 to 99 percent')
            percent = float(input(': '))
            if 1 < percent < 99:
                pass

            else:
                return print('Waring: The percent is to small or to big it should be 1 to 99 percent')

        except LengthError:
            error.show_massage()
            return False

        except ValueError:
            return print('ValueError: Your percent should be just number like 26.5 percent, try again')

        try:
            print('Enter usage limitation of your discount')
            usage_limitation = int(input(': '))

        except ValueError:
            return print('ValueError: The usage limitation should be just number')

        # Process of choose start_date
        print('Enter start date of your discount like 2008-12-7 else don\'t type anything')
        start_date = input(': ')
        if len(start_date) == 0:
            start_date = None

        else:
            pattern = '[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}'
            result_pattern = re.search(pattern, start_date)
            if result_pattern is not None:
                start_date = start_date.split('-')
                try:
                    start_date = date(year=int(start_date[0]),
                                      month=int(start_date[1]),
                                      day=int(start_date[2]))

                except ValueError:
                    return print('ValeError: Month or day is out of rang')

            else:
                return print('Pattern of your start date should be like 2001-1-1')

        # Process of choose expire_date
        print('Enter expire date of your discount like 2008-12-7 else don\'t type anything')
        expire_date = input(': ')
        if len(expire_date) == 0:
            expire_date = None

        else:
            pattern = '[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}'
            result_pattern = re.search(pattern, expire_date)
            if result_pattern is not None:
                expire_date = expire_date.split('-')
                try:
                    expire_date = date(year=int(expire_date[0]), month=int(expire_date[1]), day=int(expire_date[2]))

                except ValueError:
                    return print('ValueError: Month or day is out of rang')

            else:
                return print('Pattern of your expire date should be like 2001-1-1')

        print('Enter description of your discount else don\'t type anything')
        description = input(': ')
        if len(description) == 0:
            description = None

        discount = cls(start_date=start_date, expire_date=expire_date, title=title,
                       percent=percent, code=code, description=description, usage_limitation=usage_limitation)
        with Session() as session:
            session.add(discount)

            session.commit()

        print(f'Discount successfully Added and it\' code is {code}')

    @classmethod
    def generate_code(cls):
        proceed_duplicated_code = False
        while proceed_duplicated_code is False:
            # This process is for making code of our discount
            code = ''
            while len(code) != 3:
                code = code + random.choice(string.ascii_letters)

            while len(code) != 6:
                code = code + random.choice(string.digits)

            code = code + str(ord(random.choice(string.ascii_letters)))

            while len(code) != 10:
                code = code + random.choice(character_for_discount_code)

            with Session() as session:
                result = session.query(cls).filter(cls.code == code).all()

            if len(result) == 0:
                return code

    @classmethod
    def delete(cls):
        print('Enter id of your discount that you want to delete')
        try:
            id_discount = int(input(': '))

        except ValueError:
            return print('ValueError: Your id should be just number')

        with Session() as session:
            result = session.query(cls).filter(cls.id == id_discount).delete

        if result == 1:
            print('Discount successfully deleted')

        else:
            print('Waring: Discount id not found')

