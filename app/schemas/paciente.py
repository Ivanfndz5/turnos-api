from pydantic import BaseModel
from datetime import datetime


class PacienteBase(BaseModel):
    nombre:str
    telefono:str
    email :str

class PacienteCreate(PacienteBase):
    pass

class PacienteUpdate(BaseModel):
    nombre:str | None = None
    telefono:str | None = None
    email:str    | None = None

class PacienteResponse(PacienteBase):
    creado:datetime


