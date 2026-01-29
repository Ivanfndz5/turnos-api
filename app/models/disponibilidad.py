from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from app.db.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime



class Disponibilidad(Base):
    __tablename__= 'disponibilidades'
    id = Column(Integer,primary_key=True, index= True)
    inicio = Column(DateTime, nullable=False)
    fin = Column(DateTime, nullable = False)
    creado = Column(DateTime, default=datetime.utcnow)
    actualizado = Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    doctor_id = Column(Integer, ForeignKey('doctores.id'), nullable=False)
    doctor = relationship('Doctor', back_populates='disponibilidades')

