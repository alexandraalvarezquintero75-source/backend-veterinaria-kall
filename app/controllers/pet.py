from sqlalchemy.orm import Session
from app.models.pet import Pet as PetModel
from app.schemas.pet import PetCreate

def create_pet(db: Session, pet: PetCreate):
    try:
        db_pet = PetModel(**pet.dict())
        db.add(db_pet)
        db.commit()
        db.refresh(db_pet)
        return db_pet
    except Exception as e:
        db.rollback()
        print("❌ Error en create_pet:", e)
        raise


def get_pets(db: Session, skip: int = 0, limit: int = 10):
    return db.query(PetModel).offset(skip).limit(limit).all()

def get_pet(db: Session, pet_id: int):
    return db.query(PetModel).filter(PetModel.id == pet_id).first()

def update_pet(db: Session, pet_id: int, pet_data: PetCreate):
    pet = db.query(PetModel).filter(PetModel.id == pet_id).first()
    if pet:
        for key, value in pet_data.dict().items():
            setattr(pet, key, value)
        db.commit()
        db.refresh(pet)
    return pet

def delete_pet(db: Session, pet_id: int):
    pet = db.query(PetModel).filter(PetModel.id == pet_id).first()
    if pet:
        db.delete(pet)
        db.commit()
    return pet
