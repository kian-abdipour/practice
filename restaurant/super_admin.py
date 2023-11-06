from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship
from base import Base


class SuperAdmin(Base):
    __tablename__ = 'superadmin'
    superadmin_id = Column('superadmin_id', Integer, primary_key=True, nullable=False, unique=True)
    first_name = Column('first_name', VARCHAR(30))
    last_name = Column('last_name', VARCHAR(30))
    admin = relationship('Admin')

