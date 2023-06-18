from fastapi import Depends

from pymongo.database import Database

from models.reservation import HotelReservation
from schemas.reservation import reservationUpdate

async def create_reservation(db:Database, model:HotelReservation):
    dict_model = model.dict()
    # Getting the last reservation
    last_model = [reservation async for reservation in db.Reservations.find().sort("_id", -1).limit(1)]

    # Creating the new _id for the new Registration
    if not last_model:
        dict_model[0]["_id"] = 1
    else:
        dict_model["_id"] = last_model[0]["_id"]+1
    
    result = await db.Reservations.insert_one(dict_model)
    if result.inserted_id:
        return {"Result": "Success"}
    else:
        return {"Result": "Error"}

async def get_all_reservations(db:Database):
    reservations = [reservation async for reservation in db.Reservations.find()]
    return reservations

async def update_reservation(db:Database, reservation_id:int, model_update:reservationUpdate):
    result = await db.Reservations.update_one({"_id": reservation_id}, {"$set": model_update.dict(exclude_unset=True)})
    if result.modified_count > 0:
        return {"Result": "Success"}
    else:
        return {"Result": "Error"}

async def delete_reservation(db:Database, reservation_id:int):
    result = await db.Reservations.delete_one({"_id": reservation_id})
    if result.deleted_count == 1:
        return {"Result": "Success"}
    else:
        return {"Result": "Error"}