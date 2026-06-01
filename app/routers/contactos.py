from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Contacto(BaseModel):
    id: int
    nombre: str
    email: str
    telefono: str

contactos_db = [
    Contacto(id=1, nombre="Carlos Pérez", email="carlos@example.com", telefono="123-456-7890"),
    Contacto(id=2, nombre="Ana Gómez", email="ana@example.com", telefono="098-765-4321"),
]

@router.get("/contactos", response_model=List[Contacto])
async def get_contactos():
    return contactos_db

@router.post("/contactos", response_model=Contacto)
async def create_contacto(contacto: Contacto):
    contactos_db.append(contacto)
    return contacto

@router.get("/contactos/{contacto_id}", response_model=Contacto)
async def get_contacto(contacto_id: int):
    for contacto in contactos_db:
        if contacto.id == contacto_id:
            return contacto
    raise HTTPException(status_code=404, detail="Contacto not found")

@router.put("/contactos/{contacto_id}", response_model=Contacto)
async def update_contacto(contacto_id: int, contacto: Contacto):
    for index, existing_contacto in enumerate(contactos_db):
        if existing_contacto.id == contacto_id:
            contactos_db[index] = contacto
            return contacto
    raise HTTPException(status_code=404, detail="Contacto not found")

@router.delete("/contactos/{contacto_id}", response_model=Contacto)
async def delete_contacto(contacto_id: int):
    for index, contacto in enumerate(contactos_db):
        if contacto.id == contacto_id:
            return contactos_db.pop(index)
    raise HTTPException(status_code=404, detail="Contacto not found")
