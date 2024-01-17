from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from restaurant.modul.base import Base
from restaurant.modul import (super_admin, admin, category, item, category_item,
                              customer, order, order_item, payment, super_admin)


engine = create_engine('postgresql+psycopg2://kian:bmw1386z4@localhost:5432/restaurant', echo=False)
Session = sessionmaker(engine)
