from fastapi import APIRouter, status, Depends

from pymongo.database import Database

from ...deps import get_async_db
from crud.crud_reservations import get_all_reservations, create_reservation, update_reservation, delete_reservation
from models.reservation import HotelReservation
from schemas.reservation import reservationUpdate

router = APIRouter()

@router.post(
    path="/",
    status_code= status.HTTP_200_OK
)
async def create(
    model:HotelReservation,
    db:Database = Depends(get_async_db)
):
    return await create_reservation(db, model)

@router.get(
    path="/",
    status_code= status.HTTP_200_OK
)
async def read_all(
    db:Database = Depends(get_async_db)
):
    return await get_all_reservations(db)

@router.put(
    path="/{reservation_id}",
    status_code= status.HTTP_200_OK
)
async def update_one_reservation(
    model_update: reservationUpdate,
    reservation_id: int,
    db:Database = Depends(get_async_db)
):
    return await update_reservation(db, reservation_id, model_update)

@router.delete(
    path="/{reservation_id}",
    status_code=status.HTTP_200_OK
)
async def delete_one_reservation(
    reservation_id: int,
    db:Database = Depends(get_async_db)
):
    return await delete_reservation(db, reservation_id)