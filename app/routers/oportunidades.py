from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Oportunidad(BaseModel):
    id: int
    nombre: str
    valor: float
    etapa: str

oportunidades_db = [
    Oportunidad(id=1, nombre="Oportunidad A", valor=10000.0, etapa="Inicial"),
    Oportunidad(id=2, nombre="Oportunidad B", valor=20000.0, etapa="Propuesta"),
]

@router.get("/oportunidades", response_model=List[Oportunidad])
async def get_oportunidades():
    return oportunidades_db

@router.post("/oportunidades", response_model=Oportunidad)
async def create_oportunidad(oportunidad: Oportunidad):
    oportunidades_db.append(oportunidad)
    return oportunidad

@router.get("/oportunidades/{oportunidad_id}", response_model=Oportunidad)
async def get_oportunidad(oportunidad_id: int):
    for oportunidad in oportunidades_db:
        if oportunidad.id == oportunidad_id:
            return oportunidad
    raise HTTPException(status_code=404, detail="Oportunidad not found")

@router.put("/oportunidades/{oportunidad_id}", response_model=Oportunidad)
async def update_oportunidad(oportunidad_id: int, oportunidad: Oportunidad):
    for index, existing_oportunidad in enumerate(oportunidades_db):
        if existing_oportunidad.id == oportunidad_id:
            oportunidades_db[index] = oportunidad
            return oportunidad
    raise HTTPException(status_code=404, detail="Oportunidad not found")

@router.delete("/oportunidades/{oportunidad_id}", response_model=Oportunidad)
async def delete_oportunidad(oportunidad_id: int):
    for index, oportunidad in enumerate(oportunidades_db):
        if oportunidad.id == oportunidad_id:
            return oportunidades_db.pop(index)
    raise HTTPException(status_code=404, detail="Oportunidad not found")
