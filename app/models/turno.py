from sqlalchemy import DateTime, String, Integer, Boolean, Column, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
from enum import Enum
from datetime import datetime
from enum import Enum as PyEnum
from sqlalchemy import Enum as SQLEnum

class EstadoTurno(Enum):
    RESERVADO = 'Reservado'
    CONFIRMADO = 'Confirmado'
    COMPLETADO = 'Completado'
    CANCELADO = 'Cancelado'
    NO_SHOW = 'No asistido'


class Turno(Base):
    __tablename__ = 'turnos'

    id = Column(Integer,primary_key=True, index= True)
    inicio = Column(DateTime, nullable= False)
    fin = Column(DateTime, nullable= False)

    estado = Column(
        SQLEnum(EstadoTurno,name='estado turno'),
        default=EstadoTurno.RESERVADO,
        nullable=False

    )
    #default= means que si no le pasamos ningun valor al crearlo queda como reservado

    paciente_id = Column(Integer,ForeignKey('pacientes.id'))
    paciente = relationship('Paciente',back_populates='turnos')

    doctor_id = Column(Integer, ForeignKey('doctores.id'))
    doctor = relationship('Doctor', back_populates='turnos')

    creado = Column(DateTime, default=datetime.utcnow)
    actualizado = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


