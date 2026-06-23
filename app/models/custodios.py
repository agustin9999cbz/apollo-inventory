from pydantic import BaseModel


class CustodioCreate(BaseModel):
    nombre: str


class Custodio(BaseModel):
    id: str
    nombre: str