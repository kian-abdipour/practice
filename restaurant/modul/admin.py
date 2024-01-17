from sqlalchemy import Column, Integer, Unicode, ForeignKey
from restaurant.modul.base import Base
from restaurant.modul.mixin import DateTimeMixin


class Admin(DateTimeMixin, Base):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode(30), nullable=False)
    last_name = Column(Unicode(30), nullable=False)
    username = Column(Unicode(16), unique=True, nullable=False)
    password = Column(Unicode(8), nullable=False)
    superadmin_id = Column(ForeignKey('super_admin.id'))

