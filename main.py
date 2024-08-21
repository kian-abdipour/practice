from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, Integer, Unicode, Column
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
from os import getenv
from sqlalchemy.sql import text

load_dotenv()
number = getenv('a')


Base = declarative_base()

engine = create_engine('postgresql+psycopg2://kian:bmw1386z4@127.0.0.1:5432/practice', echo=False)

database_session = sessionmaker(bind=engine)
session = Session(bind=engine)


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    username = Column(Unicode(20), unique=True, nullable=False)


#Base.metadata.create_all(engine)
try:
    session.begin()

    session.execute(text('BEGIN; LOCK TABLE database_version IN ACCESS EXCLUSIVE MODE;'))
    session.commit()

    customers = session.query(Customer).all()

finally:
    session.close()


print(customers)

