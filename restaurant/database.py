from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from restaurant.model.base import Base
#from restaurant.model import (super_admin, admin, category, item, category_item,
#                              customer, order, order_item, payment, super_admin, discount, discount_history)
from dotenv import load_dotenv
from os import getenv

load_dotenv()
database_url = getenv('DATABASE_URL')


engine = create_engine(database_url, echo=False)
#Base.metadata.create_all(engine)
database_session = sessionmaker(engine)


def get_session():
    session = database_session()
    try:
        yield session

    finally:
        session.close()

