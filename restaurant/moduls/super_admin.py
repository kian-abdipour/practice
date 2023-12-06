from sqlalchemy import Column, Integer, Unicode
from sqlalchemy.orm import relationship
#from restaurant.moduls.base import Base
from restaurant.moduls.mixing_modul import Moment, Base


class SuperAdmin(Base, Moment):
    __tablename__ = 'super_admin'
    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode(30))
    last_name = Column(Unicode(30))
    password = Column(Unicode(8))

    admins = relationship('Admin')

