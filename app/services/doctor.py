from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate


def crear_doctor(db:Session,doctor:DoctorCreate):
    #regla 1 nombre obligatorio
    if not doctor.nombre.strip():
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail="El nombre del profesional es obligatorio"
        )

    #regla 2 especialidad obligatoria
    if not doctor.especialidad.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail = "la especialidad es obligatoria"
        )

    #Busca en db si ya existe un doctor con la misma matricula
    existe_doctor = (
        db.query(Doctor)
        .filter(Doctor.matricula == doctor.matricula)
        .first()
    )

    if existe_doctor:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="ya existe un doctor con esa matricula"
        )

    db_doctor = Doctor(
        nombre = doctor.nombre,
        especialidad = doctor.especialidad,
        matricula= doctor.matricula
    )

    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)

    return db_doctor



def obtener_doctor(db:Session, doctor_id:int):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = "No se ha encontrado el doctor solicitado"
        )
    return doctor


