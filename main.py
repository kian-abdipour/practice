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
another_session = Session(bind=engine)


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    username = Column(Unicode(20), unique=True, nullable=False)


#Base.metadata.create_all(engine)
try:
    customer = session.query(Customer).filter(Customer.id == 11).with_for_update().all()

    customer_after_lock = another_session.query(Customer).filter(Customer.id == 11).one_or_none()
    customer_after_lock.username = 'nima'

    print(customer)

    session.commit()

finally:
    session.close()


