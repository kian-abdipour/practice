from sqlalchemy import create_engine

from restaurant.moduls.base import Base
from restaurant.moduls import SuperAdmin, Admin, Customer, Category, Item, Order, OrderItem, Payment

engine = create_engine('postgresql+psycopg2://kian:bmw1386z4@localhost:5432/restaurant', echo=True)
Base.metadata.create_all(engine)

