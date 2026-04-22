from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base

# Importar modelos para que SQLAlchemy los registre
from app.models import usuario, solicitud, documento, historial, notificacion

app = FastAPI()

# Crear tablas automáticamente
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}