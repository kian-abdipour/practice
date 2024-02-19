from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from restaurant.model.base import Base
#from restaurant.model import (super_admin, admin, category, item, category_item,
#                              customer, order, order_item, payment, super_admin)
from dotenv import load_dotenv
from os import getenv

load_dotenv()
database_url = getenv('database_url')


engine = create_engine(database_url, echo=False)
Session = sessionmaker(engine)

