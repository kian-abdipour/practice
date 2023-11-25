from sqlalchemy import Column, Integer, Unicode, ForeignKey, DateTime
from restaurant.moduls.base import Base
from datetime import datetime


class Admin(Base):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    first_name = Column(Unicode(30))
    last_name = Column(Unicode(30))
    password = Column(Unicode(8))
    superadmin_id = Column(ForeignKey('super_admin.id'))

