from sqlalchemy import Column, Integer, Unicode, ForeignKey
from restaurant.modul.base import Base
from restaurant.modul.mixin import DateTimeMixin


class Admin(DateTimeMixin, Base):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode(30))
    last_name = Column(Unicode(30))
    password = Column(Unicode(8))
    superadmin_id = Column(ForeignKey('super_admin.id'))

