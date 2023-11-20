from sqlalchemy import Column, Integer, Unicode
from sqlalchemy.orm import relationship
from base import Base


class SuperAdmin(Base):
    __tablename__ = 'superadmin'
    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode(30))
    last_name = Column(Unicode(30))

    admins = relationship('Admin')

