from sqlalchemy import Column, Integer, Boolean, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime

class Doctor(Base):
    __tablename__= 'doctores'
    id = Column(Integer,primary_key=True, index=True)
    nombre = Column(String, index=True)
    especialidad = Column(String, index=True)
    creado = Column(DateTime, default=datetime.utcnow)
    turnos = relationship('Turno', back_populates='doctor')
    actualizado = Column(DateTime, default=datetime.utcnow,)

    disponibilidades = relationship('Disponibilidad', back_populates='doctor')  # agregalo
    matricula = Column(String, unique=True, index=True)
