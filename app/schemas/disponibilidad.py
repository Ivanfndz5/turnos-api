from pydantic import BaseModel
from datetime import datetime

class DisponibilidadBase(BaseModel):
    inicio:str
    fin:str

class DisponibilidadCreate(DisponibilidadBase):
    doctor_id:int
    inicio: str
    fin:str


class DisponibilidadUpdate(BaseModel):
    inicio:str | None= None
    fin:str | None = None
    doctor_id:int | None=None

class DisponibilidadResponse(DisponibilidadBase):
    id:int
    doctor_id:int
    inicio:str
    fin:str
    creado:datetime
