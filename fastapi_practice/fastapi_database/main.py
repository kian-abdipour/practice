from fastapi_practice.fastapi_database.database import engine
from fastapi import FastAPI

from fastapi_practice.fastapi_database.router import user

from fastapi_practice.fastapi_database.model.base import Base
from fastapi_practice.fastapi_database.model.user import User

from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(engine)
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(user.router)

