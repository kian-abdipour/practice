from sqlalchemy import create_engine
from restaurant.models import SuperAdmin, Admin, Customer, Category, Item, Order, OrderItem, Base

engine = create_engine('postgresql+psycopg2://kian:bmw1386z4@localhost:5432/restaurant', echo=True)

