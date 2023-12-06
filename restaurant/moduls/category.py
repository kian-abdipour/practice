from sqlalchemy import Column, Integer, Unicode
from sqlalchemy.orm import relationship
#from restaurant.moduls.base import Base
from restaurant.moduls.mixing_modul import Moment, Base


class Category(Base, Moment):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(30))

    items = relationship('OrderItem')

