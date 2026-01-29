from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.schemas.turno import TurnoCreate
from app.db.database import get_db
from app.services.turno import crear_turno


router = APIRouter(prefix='/turnos',tags=['turnos'])


@router.post('/')
def crear_turno_endpoint(doctor_id :int,paciente_id:int,turno:TurnoCreate,db:Session = Depends(get_db)):
    return crear_turno(db,doctor_id,paciente_id,turno)
