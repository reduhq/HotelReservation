from datetime import date, datetime

from pydantic import BaseModel
from pydantic import EmailStr

class HotelReservation(BaseModel):
    NombreCliente:str
    EmailCliente:EmailStr
    TelefonoCliente:str
    FechaCheckIn:str = datetime.now().date()
    FechaCheckOut:str = datetime.now().date()
    TipoHabitacion:str
    NumeroHuespedes:int
