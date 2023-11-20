from sqlalchemy import Column, Integer, Unicode, ForeignKey
from base import Base


class Admin(Base):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode(30))
    last_name = Column(Unicode(30))
    password = Column(Unicode(8))
    superadmin_id = Column(Integer, ForeignKey('superadmin.id'))

