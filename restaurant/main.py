from sqlalchemy import create_engine

from restaurant.models import SuperAdmin, Admin

engine = create_engine('postgresql+psycopg2://kian:bmw1386z4@localhost:5432/restaurant', echo=True)

print(
      SuperAdmin,
      Admin
)
