from sqlalchemy import Column, Integer, Unicode, String, ForeignKey, Boolean
from restaurant.model.base import Base
from restaurant.model.mixin import datetime
from restaurant.database import Session
from restaurant.custom_exception import LengthError
import random, string
from restaurant.model.helper import character_for_discount_code


class Discount(datetime, Base):
    id = Column(Integer, primary_key=True)
    expire_date = Column(Boolean)
    title = Column(Unicode(40))
    percent = Column(Integer)
    code = Column(String(10))
    description = Column(Unicode)

    @classmethod
    def add(cls):
        try:
            print('Enter title of your discount')
            title = input(': ')
            if len(title) > 40:
                error = LengthError(massage='LengthError: Title is too long! try again')
                raise error

            print('Enter percent of your discount it must be number at least 2 character')
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

