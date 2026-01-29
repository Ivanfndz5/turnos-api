from app.db.database import engine, Base
#importar modelos luego
from app.models.paciente import Paciente
from app.models.doctor import Doctor
from app.models.turno import Turno
from app.models.disponibilidad import Disponibilidad


Base.metadata.create_all(bind=engine)
print('tablas creadas correctamente')

