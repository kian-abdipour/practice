from sqlalchemy import create_engine
from base import Base
from super_admin import SuperAdmin
from item import Item
from category import Category
from admin import Admin
from order import Order
from customer import Customer


engine = create_engine("postgresql+psycopg2://kian:bmw1386z4@localhost:5432/restaurant")
Base.metadata.create_all(engine)

