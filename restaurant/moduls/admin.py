from sqlalchemy import Column, Integer, Unicode, ForeignKey
#from restaurant.moduls.base import Base
from restaurant.moduls.mixing_modul import Moment, Base


class Admin(Base, Moment):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode(30))
    last_name = Column(Unicode(30))
    password = Column(Unicode(8))
    superadmin_id = Column(ForeignKey('super_admin.id'))

