from pydantic import BaseModel
from datetime import datetime

class DoctorBase(BaseModel):
    nombre:str
    especialidad:str
    matricula : str

class DoctorCreate(DoctorBase):
    pass

class DoctorUpdate(BaseModel):
    nombre:str | None=None
    especialidad:str | None=None

class DoctorResponse(DoctorBase):
    id:int
    creado:datetime