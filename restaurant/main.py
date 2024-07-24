from fastapi import FastAPI

from contextlib import asynccontextmanager

from restaurant.model.base import Base
from restaurant.database import engine
from restaurant.router import customer


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router=customer.router)

