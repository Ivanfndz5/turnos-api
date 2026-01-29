from app.schemas.turno import TurnoCreate,TurnoUpdate
from app.models.turno import Turno
from app.models.doctor import   Doctor
from app.models.paciente import Paciente
from datetime import datetime
from fastapi import HTTPException,status
from sqlalchemy.orm import Session


def crear_turno(db:Session, doctor_id : int,paciente_id:int,turno:TurnoCreate):
    #validar que el doctor existia
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= 'doctor no encontrado'
        )

    #validar que el paciente existe
    paciente= db.query(Paciente).filter(Paciente.id == paciente_id).first()
    if not paciente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Paciente no encontrado'
        )

    #validar rango de fechas
    if turno.inicio >=turno.fin:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail =  'La hora de inicio debe ser antes de la hora de fin'
        )


    #Crear un turno

    db_turno = Turno(
        doctor_id=doctor_id,
        paciente_id=paciente_id,
        inicio=turno.inicio,
        fin = turno.fin
    )
    db.add(db_turno)
    db.commit()
    db.refresh(db_turno)

    return db_turno
