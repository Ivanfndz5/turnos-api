

from sqlalchemy import Column, Boolean,Integer,String,DateTime
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime



class Paciente(Base):
    __tablename__ = 'pacientes'
    id = Column(Integer, primary_key=True,index=True)
    nombre = Column(String, index= True, nullable=False)
    telefono = Column(String, index= True, nullable=False)
    email = Column(String, unique=True, nullable= False)
    creado = Column(DateTime, default= datetime.utcnow)

    turnos = relationship('Turno',back_populates='paciente')


