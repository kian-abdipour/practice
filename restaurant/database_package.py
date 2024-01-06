from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from restaurant.modul.base import Base


engine = create_engine('postgresql+psycopg2://kian:bmw1386z4@localhost:5432/restaurant', echo=False)
Session = sessionmaker(engine)

