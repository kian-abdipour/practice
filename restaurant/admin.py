from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from base import Base


class Admin(Base):
    __tablename__ = 'admin'
    admin_id = Column('admin_id', Integer, primary_key=True, nullable=False, unique=True)
    first_name = Column('first_name', VARCHAR(30))
    last_name = Column('last_name', VARCHAR(30))
    superadmin_id = Column("superadmin_id", Integer, ForeignKey('superadmin.superadmin_id'))

