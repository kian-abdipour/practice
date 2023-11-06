from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship
from base import Base


class Category(Base):
    __tablename__ = 'category'
    category_id = Column('category_id', Integer, primary_key=True, nullable=False, unique=True)
    name = Column('name', VARCHAR(30))
    item = relationship('Item')

