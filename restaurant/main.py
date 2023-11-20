from sqlalchemy import create_engine

from restaurant.models import order, order_item, base
from restaurant.models.admin import Admin
from restaurant.models.category import Category
from restaurant.models.customer import Customer
from restaurant.models.item import Item
from restaurant.models.superadmin import SuperAdmin

engine = create_engine('postgresql+psycopg2://kian:bmw1386z4@localhost:5432/restaurant', echo=True)


print(SuperAdmin,
      Admin,
      Customer,
      Category,
      Item,
      order,
      order_item,
      base)

