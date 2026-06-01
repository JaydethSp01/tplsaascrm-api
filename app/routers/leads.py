from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Lead(BaseModel):
    id: int
    name: str
    email: str
    phone: str

leads_db = [
    Lead(id=1, name="John Doe", email="john@example.com", phone="123-456-7890"),
    Lead(id=2, name="Jane Smith", email="jane@example.com", phone="098-765-4321"),
]

@router.get("/leads", response_model=List[Lead])
async def get_leads():
    return leads_db

@router.post("/leads", response_model=Lead)
async def create_lead(lead: Lead):
    leads_db.append(lead)
    return lead

@router.get("/leads/{lead_id}", response_model=Lead)
async def get_lead(lead_id: int):
    for lead in leads_db:
        if lead.id == lead_id:
            return lead
    raise HTTPException(status_code=404, detail="Lead not found")

@router.put("/leads/{lead_id}", response_model=Lead)
async def update_lead(lead_id: int, lead: Lead):
    for index, existing_lead in enumerate(leads_db):
        if existing_lead.id == lead_id:
            leads_db[index] = lead
            return lead
    raise HTTPException(status_code=404, detail="Lead not found")

@router.delete("/leads/{lead_id}", response_model=Lead)
async def delete_lead(lead_id: int):
    for index, lead in enumerate(leads_db):
        if lead.id == lead_id:
            return leads_db.pop(index)
    raise HTTPException(status_code=404, detail="Lead not found")
