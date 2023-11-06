from sqlalchemy import create_engine
from base import Base
import __init__

engine = create_engine("postgresql+psycopg2://kian:bmw1386z4@localhost:5432/restaurant", echo=True)
Base.metadata.create_all(engine)

