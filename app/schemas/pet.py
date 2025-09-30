from pydantic import BaseModel
from datetime import date
from typing import Optional

class PetBase(BaseModel):
    name: str
    especie: str
    raza: Optional[str] = None
    sexo: Optional[str] = None
    nacimiento: Optional[date] = None
    caracteristicas: Optional[str] = None
    dueno: str
    foto: Optional[str] = None

class PetCreate(PetBase):
    pass

class Pet(PetBase):
    id: int

    class Config:
        from_attributes = True  # Pydantic v2 (antes orm_mode = True)
