from sqlalchemy import Column, Integer, Unicode
from sqlalchemy.orm import relationship
from restaurant.modul.base import Base
from restaurant.modul.mixin import DateTimeMixin


class SuperAdmin(DateTimeMixin, Base):
    __tablename__ = 'super_admin'
    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode(30))
    last_name = Column(Unicode(30))
    password = Column(Unicode(8))

    admins = relationship('Admin')

