from admin import Admin
import sqlalchemy as sa
from sqlalchemy import *
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm import relationship

Base = declarative_base()


class SuperAdmin(Base):
    __tablename__ = 'superadmins'
    superadmin_id = Column('superadmin_id', sa.Integer, primary_key=True, nullable=False, unique=True)
    first_name = Column('first_name', sa.VARCHAR(30))
    last_name = Column('last_name', sa.VARCHAR(30))
    admin = relationship('Admin')

