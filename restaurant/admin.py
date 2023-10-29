import sqlalchemy as sa
from sqlalchemy import *
from base import Base


class Admin(Base):
    __tablename__ = 'admins'
    admin_id = Column('admin_id', sa.INTEGER, primary_key=True, nullable=False, unique=True)
    first_name = Column('first_name', sa.VARCHAR(30))
    last_name = Column('last_name', sa.VARCHAR(30))
    superadmin_id = Column('superadmin_id', sa.INTEGER, ForeignKey('superadmins.superadmin_id'))

