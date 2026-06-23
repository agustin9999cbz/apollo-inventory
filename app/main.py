# app/main.py

from fastapi import FastAPI
from app.routers import activos
from app.routers import custodios

app = FastAPI(title="Apollo Inventory")

app.include_router(
    activos.router,
    prefix="/activos",
    tags=["Activos"]
)
app.include_router(
    custodios.router,
    prefix="/custodios",
    tags=["Custodios"]
)


@app.get("/")
def home():
    return {"sistema": "Apollo Inventory"}