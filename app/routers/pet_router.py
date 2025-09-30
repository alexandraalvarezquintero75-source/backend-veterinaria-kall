from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud
from app.schemas.pet import Pet, PetCreate
from app.database import get_db

router = APIRouter(prefix="/v1/pet", tags=["pet"])

# Crear mascota
@router.post("/caut", response_model=Pet)
def create_pet(pet: PetCreate, db: Session = Depends(get_db)):
    return crud.create_pet(db=db, pet=pet)

# Listar mascotas
@router.get("/gaut", response_model=List[Pet])
def read_pets(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_pets(db, skip=skip, limit=limit)

# Obtener mascota por ID
@router.get("/gaut/{pet_id}", response_model=Pet)
def read_pet(pet_id: int, db: Session = Depends(get_db)):
    db_pet = crud.get_pet(db, pet_id=pet_id)
    if db_pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    return db_pet

# Actualizar mascota
@router.put("/uaut/{pet_id}", response_model=Pet)
def update_pet(pet_id: int, pet: PetCreate, db: Session = Depends(get_db)):
    db_pet = crud.update_pet(db, pet_id=pet_id, pet_data=pet)
    if db_pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    return db_pet

# Eliminar mascota
@router.delete("/daut/{pet_id}")
def delete_pet(pet_id: int, db: Session = Depends(get_db)):
    db_pet = crud.delete_pet(db, pet_id=pet_id)
    if db_pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    return {"message": "Pet deleted successfully"}
