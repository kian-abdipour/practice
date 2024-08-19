from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from restaurant.model.base import Base
from dotenv import load_dotenv
from os import getenv

load_dotenv()
database_url = getenv('DATABASE_URL')

engine = create_engine(database_url, echo=False)

database_session = sessionmaker(bind=engine)


def get_session():
    session = database_session()
    try:
        yield session

    finally:
        session.close()

