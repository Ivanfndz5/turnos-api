from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.schemas.disponibilidad import DisponibilidadCreate
from app.services.disponibilidad import crear_disponibilidad
from app.db.database import get_db

router = APIRouter(prefix='/disponibilidades',tags=['disponibilidades'])

@router.post('/')

def crear_disponibilidad_endpoint(doctor_id:int,disponibilidad:DisponibilidadCreate, db:Session=Depends(get_db)):
    return crear_disponibilidad(db,doctor_id,disponibilidad)

