from fastapi import status,HTTPException
from sqlalchemy.orm import Session
from app.models.disponibilidad import Disponibilidad
from app.schemas.disponibilidad import DisponibilidadCreate
from app.services.doctor import obtener_doctor
from datetime import datetime

def crear_disponibilidad(db:Session,doctor_id:int,disponibilidad:DisponibilidadCreate):
    #validar que el doctor exista
    doctor=obtener_doctor(db,doctor_id)

    #validad que la franja tenga fecha y hora concretas
    if disponibilidad.inicio > disponibilidad.fin:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="la hora de inicio debe ser antes de la hora de fin"
        )

    #trae las franjas existentes
    franjas_existentes=(
        db.query(Disponibilidad)
        .filter(Disponibilidad.doctor_id == doctor_id)
        .all()
    )

    for franja in franjas_existentes:
        if(disponibilidad.inicio <franja.fin and disponibilidad.fin> franja.inicio):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="la franja de disponibilidad se solapa con otra existente"

             )


    #creando disponibilidad
    db_disponibilidad = Disponibilidad(
        doctor_id =doctor_id,
        inicio= disponibilidad.inicio,
        fin= disponibilidad.fin
    )

    db.add(db_disponibilidad)
    db.commit()
    db.refresh(db_disponibilidad)

    return db_disponibilidad