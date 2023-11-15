from sqlalchemy import Column, Integer, Unicode
from sqlalchemy.orm import relationship
from base import Base


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(30))
    items = relationship('Item')

