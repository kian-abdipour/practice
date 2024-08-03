import datetime
import random
import re
import string
from datetime import date

from sqlalchemy import Column, Integer, Unicode, String, Float, Date, Boolean
from sqlalchemy.orm import relationship, Session

from restaurant.custom_exception import LengthError, DisposableDiscountError, StartDateDiscountError, \
    ExpireDateDiscountError, UsageLimitationDiscountError
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
    code = Column(String(10), nullable=False, unique=True)
    description = Column(Unicode)
    usage_limitation = Column(Integer)
    disposable = Column(Boolean)

    discount_histories = relationship('DiscountHistory', back_populates='discount')

    @classmethod
    def add(
            cls, session: Session, start_date, expire_date, title,
            percent, code, description, usage_limitation, disposable
    ):
        discount = cls(start_date=start_date, expire_date=expire_date, title=title, percent=percent,
                       code=code, description=description, usage_limitation=usage_limitation, disposable=disposable)
        session.add(discount)

        session.commit()
        session.refresh(discount)

        return discount

    @classmethod
    def generate_code(cls, session: Session):
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

    @classmethod
    def search_by_code(cls, session: Session, code):
        result = session.query(cls).filter(cls.code == code).one_or_none()

        return result

    @classmethod
    def show_all(cls, session: Session):
        discounts = session.query(cls).all()

        return discounts

    @classmethod
    def apply_discount(cls, discount, amount):
        if discount.disposable is False:
            raise DisposableDiscountError('')

        if discount.start_date > date.today():
            raise StartDateDiscountError('')

        if discount.expire_date < date.today():
            raise ExpireDateDiscountError('')

        if discount.usage_limitation == 0:
            raise UsageLimitationDiscountError('')

        amount = amount - (discount.percent * amount)

        return amount

    @classmethod
    def decrease_usage_limitation(cls, session: Session, discount_id):
        session.query(cls).filter(cls.id == discount_id).update({cls.usage_limitation: cls.usage_limitation - 1})
        session.commit()

    @classmethod
    def search_by_id(cls, session: Session, discount_id):
        discount = session.query(cls).filter(cls.id == discount_id).one_or_none()

        return discount

    @classmethod
    def update_disposable(cls, discount_id, disposable, session):
        discount = cls.search_by_id(session=session, discount_id=discount_id)
        if disposable == 'false':
            disposable = False

        if disposable == 'true':
            disposable = True

        session.query(cls).filter(cls.id == discount_id).update({cls.disposable: disposable})

        session.commit()
        session.refresh(discount)

        return discount

