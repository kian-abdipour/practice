from sqlalchemy import Column, Integer, Unicode, String, Float, Date
from sqlalchemy.orm import relationship
from restaurant.model.base import Base
from restaurant.model.mixin import datetime
#from restaurant.database import Session
from restaurant.custom_exception import LengthError
import random, string
from restaurant.model.helper import character_for_discount_code


class Discount(datetime, Base):
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
    def add(cls):
        try:
            print('Enter title of your discount')
            title = input(': ')
            if len(title) > 40:
                error = LengthError(massage='LengthError: Title is too long! try again')
                raise error

            print('Enter percent of your discount it must be number at least 2 character between 1 to 99 percent')
            percent = int(input(': '))
            if len(str(percent)) > 2:
                error = LengthError(massage='LengthError: Percent is too long it must be just 2 character! try again')
                raise error

        except LengthError:
            error.show_massage()
            return False

        except ValueError:
            print('ValueError: Your percent should be just number, try again')

        print('Enter description of your discount')
        description = input(': ')

        # This process is for making code of our discount
        code = ''
        while len(code) != 3:
            code = code + random.choice(string.ascii_letters)

        while len(code) != 6:
            code = code + random.choice(string.digits)

        code = code + str(ord(random.choice(string.ascii_letters)))

        while len(code) != 10:
            code = code + random.choice(character_for_discount_code)
