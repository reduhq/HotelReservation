from datetime import datetime

from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr


class reservationUpdate(BaseModel):
    EmailCliente:Optional[EmailStr]
    TelefonoCliente:Optional[str]
    FechaCheckIn:Optional[str] = str(datetime.now().date())
    FechaCheckOut:Optional[str] = str(datetime.now().date())
    TipoHabitacion:Optional[str]
    NumeroHuespedes:Optional[int]
