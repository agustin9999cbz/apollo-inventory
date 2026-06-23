from fastapi import APIRouter
from app.models.custodios import Custodio, CustodioCreate

router = APIRouter()

custodios_db = []


@router.post("/", response_model=Custodio)
def crear_custodio(data: CustodioCreate):

    nuevo = Custodio(
        id=f"CUS-{len(custodios_db)+1:03}",
        nombre=data.nombre
    )

    custodios_db.append(nuevo)

    return nuevo


@router.get("/")
def listar_custodios():
    return custodios_db