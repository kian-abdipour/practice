from sqlalchemy import create_engine
from restaurant.modul.base import Base
from restaurant.modul import (SuperAdmin, Admin, Customer, Category, Item,
                              Order, OrderItem, Payment, Address, category_item)

engine = create_engine('postgresql+psycopg2://kian:bmw1386z4@localhost:5432/restaurant', echo=False)
Base.metadata.create_all(engine)

