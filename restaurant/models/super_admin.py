from sqlalchemy import Column, Integer, Unicode, DateTime
from sqlalchemy.orm import relationship
from base import Base
from datetime import datetime


class SuperAdmin(Base):
    __tablename__ = 'super_admin'
    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode(30), nullable=False)
    last_name = Column(Unicode(30), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    admins = relationship('Admin')

