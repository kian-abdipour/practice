import sqlalchemy as sa
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Category(Base):
    __tablename__ = 'categories'
    category_id = Column('category_id', sa.INTEGER, primary_key=True, nullable=False, unique=True)
    name = Column('name', sa.VARCHAR(30))
    item = relationship('Item')

