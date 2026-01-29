from fastapi import FastAPI
from app.routers import turno,disponibilidades,paciente,doctor


app = FastAPI()

app.include_router(turno.router)
app.include_router(disponibilidades.router)
app.include_router(paciente.router)
app.include_router(doctor.router)


