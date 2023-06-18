from fastapi import APIRouter
from .endpoints import reservations

api_router = APIRouter()
api_router.include_router(reservations.router, prefix='/reservations', tags=['Reservations'])