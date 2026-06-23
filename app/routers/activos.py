from fastapi import APIRouter, HTTPException
from app.models.activos import ActivoCreate, Activo

router = APIRouter()

activos_db = []


@router.get("/")
def listar_activos():
    return activos_db


@router.post("/", response_model=Activo)
def crear_activo(datos: ActivoCreate):

    nuevo_activo = Activo(
        id=f"ACT-{len(activos_db)+1:03}",
        nombre=datos.nombre,
        categoria=datos.categoria,
        estado="disponible"
    )

    activos_db.append(nuevo_activo)

    return nuevo_activo

@router.get("/{activo_id}", response_model=Activo)
def obtener_activo(activo_id: str):

    for activo in activos_db:
        if activo.id == activo_id:
            return activo

    raise HTTPException(
        status_code=404,
        detail=f"Activo {activo_id} no encontrado"
    )