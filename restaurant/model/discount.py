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

