import uvicorn
from fastapi import FastAPI

from contextlib import asynccontextmanager

from restaurant.model.base import Base
from restaurant.database import engine
from restaurant.router import customer, address, admin, cart, category, category_item, item, order, payment, \
                              super_admin, discount

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router=customer.router)
app.include_router(router=address.router)
app.include_router(router=super_admin.router)
app.include_router(router=admin.router)
app.include_router(router=item.router)
app.include_router(router=cart.router)
app.include_router(router=category.router)
app.include_router(router=category_item.router)
app.include_router(router=order.router)
app.include_router(router=payment.router)
app.include_router(router=discount.router)

