from pydantic import BaseModel

class ActivoCreate(BaseModel):
    nombre: str
    categoria: str

class Activo(BaseModel):
    id: str
    nombre: str
    categoria: str
    estado: str = "disponible"