from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.schemas.paciente import PacienteCreate
from app.services.paciente import crear_paciente
from app.db.database import get_db


router = APIRouter(prefix='/pacientes',tags=['pacientes'])

@router.post('/')
def crear_paciente_endpoint( paciente:PacienteCreate, db:Session = Depends(get_db)):
    print("DEBUG paciente recibido:", paciente.dict())
    return crear_paciente(db,paciente)




