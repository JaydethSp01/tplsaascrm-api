from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Actividad(BaseModel):
    id: int
    descripcion: str
    fecha: str
    estado: str

actividades_db = [
    Actividad(id=1, descripcion="Llamada con cliente", fecha="2023-10-01", estado="Completada"),
    Actividad(id=2, descripcion="Reunión de seguimiento", fecha="2023-10-05", estado="Pendiente"),
]

@router.get("/actividades", response_model=List[Actividad])
async def get_actividades():
    return actividades_db

@router.post("/actividades", response_model=Actividad)
async def create_actividad(actividad: Actividad):
    actividades_db.append(actividad)
    return actividad

@router.get("/actividades/{actividad_id}", response_model=Actividad)
async def get_actividad(actividad_id: int):
    for actividad in actividades_db:
        if actividad.id == actividad_id:
            return actividad
    raise HTTPException(status_code=404, detail="Actividad not found")

@router.put("/actividades/{actividad_id}", response_model=Actividad)
async def update_actividad(actividad_id: int, actividad: Actividad):
    for index, existing_actividad in enumerate(actividades_db):
        if existing_actividad.id == actividad_id:
            actividades_db[index] = actividad
            return actividad
    raise HTTPException(status_code=404, detail="Actividad not found")

@router.delete("/actividades/{actividad_id}", response_model=Actividad)
async def delete_actividad(actividad_id: int):
    for index, actividad in enumerate(actividades_db):
        if actividad.id == actividad_id:
            return actividades_db.pop(index)
    raise HTTPException(status_code=404, detail="Actividad not found")
