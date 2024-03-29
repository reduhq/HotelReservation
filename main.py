from fastapi import FastAPI
from db.session import client
from api.api_v1.api import api_router

app = FastAPI()

app.include_router(api_router)