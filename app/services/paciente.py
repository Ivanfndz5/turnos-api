from fastapi import status,HTTPException
from sqlalchemy.orm import Session
from app.models.paciente import Paciente
from app.schemas.paciente import PacienteCreate



def crear_paciente(db:Session,paciente: PacienteCreate):
    nombre = paciente.nombre.strip()

    if not nombre:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail="el nombre no puede estar vacio"
        )

    paciente_existente = (
        db.query(Paciente)
        .filter(Paciente.nombre == nombre)
        .first()
    )

    if paciente_existente:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail = "El paciente ya existe"
        )

    db_paciente = Paciente(
        nombre=nombre,
        telefono=paciente.telefono,
        email=paciente.email
    )

    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)

    return db_paciente




def obtener_paciente(db:Session,paciente_id:int):
    paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()

    if not paciente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = "paciente no encontrado"
        )

    return paciente






