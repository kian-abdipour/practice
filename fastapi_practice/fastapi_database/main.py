from fastapi import FastAPI

from fastapi_practice.fastapi_database.router import user


app = FastAPI()
app.include_router(user.router)

