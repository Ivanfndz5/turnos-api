from datetime import datetime
from pydantic import BaseModel

from app.schemas.paciente import PacienteResponse


class TurnoBase(BaseModel):
    fecha_hora:datetime
    inicio :datetime
    fin: datetime

class TurnoCreate(TurnoBase):
    paciente_id:int #Recordá que el cliente necesita enviar paciente_id

class TurnoUpdate(BaseModel):
    fecha_hora:datetime | None = None
    paciente_id :str

class TurnoResponse(TurnoBase):
    id:int
    paciente:PacienteResponse #metemos toda la info del paciente
    creado: datetime

