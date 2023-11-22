from sqlalchemy import Column, Integer, Unicode, ForeignKey, DateTime
from restaurant.moduls.base import Base
from datetime import datetime


class Admin(Base):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode(30), nullable=False)
    last_name = Column(Unicode(30), nullable=False)
    password = Column(Unicode(8), nullable=False)
    superadmin_id = Column(Integer, ForeignKey('super_admin.id'))
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

