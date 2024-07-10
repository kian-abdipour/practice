from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
from os import getenv

from fastapi_practice.fastapi_database.model.base import Base
#from fastapi_practice.fastapi_database.model import user

load_dotenv()
database_url = getenv('DATABASE_URL')

engine = create_engine(url=database_url, echo=True)
database_Session = sessionmaker(engine)
#Base.metadata.create_all(engine)

