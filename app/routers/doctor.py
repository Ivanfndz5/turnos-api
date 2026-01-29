from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.schemas.doctor import DoctorCreate
from app.services.doctor import crear_doctor
from app.db.database import get_db

router= APIRouter(prefix='/doctores',tags=['doctores'])

@router.post('/')
def crear_doctor_endpoint(doctor:DoctorCreate, db:Session = Depends(get_db)):
    return crear_doctor(db,doctor)



