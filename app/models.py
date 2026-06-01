from pydantic import BaseModel

class Lead(BaseModel):
    id: int
    name: str
    email: str

class Opportunity(BaseModel):
    id: int
    title: str
    stage: str

class Contact(BaseModel):
    id: int
    name: str
    phone: str

class Activity(BaseModel):
    id: int
    description: str
