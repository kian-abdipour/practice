from sqlalchemy import create_engine

from restaurant.models import superadmin, admin, customer, category, item, order, order_item, base

engine = create_engine('postgresql+psycopg2://kian:bmw1386z4@localhost:5432/restaurant', echo=True)

print(superadmin,
      admin,
      customer,
      category,
      item,
      order,
      order_item,
      base)

