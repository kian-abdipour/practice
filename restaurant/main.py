from sqlalchemy import create_engine, text, select
from restaurant.modul.base import Base
from restaurant.modul import (SuperAdmin, Admin, Customer, Category, Item,
                              Order, OrderItem, Payment, Address, category_item)
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine('postgresql+psycopg2://kian:bmw1386z4@localhost:5432/restaurant', echo=False)
Base.metadata.create_all(engine)

super_admin_sm = SuperAdmin(first_name='lionel', last_name='messi', password='10soccer')


def get_super_admins():
    with Session(engine) as session:
        rows = session.execute(select(SuperAdmin.id, SuperAdmin.first_name,
                                      SuperAdmin.last_name, SuperAdmin.created_at).where(SuperAdmin.id == 1))

    for super_admin in rows:
        print(super_admin)


def add_super_admin(super_admin):
    with Session(engine) as session:
        session.add(super_admin)
        session.commit()


#get_super_admins()
#add_super_admin(super_admin_sm)


#print(select(SuperAdmin).where(SuperAdmin.id == 1))



with Session(engine) as session:
    super_admins = session.execute(text('select * from super_admin'))
    for item in super_admins:
        print(item[0])
