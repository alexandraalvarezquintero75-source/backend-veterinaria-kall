# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List
# from app import crud
# from app.schemas.client import Client, ClientCreate
# from app.database import get_db

# router = APIRouter(prefix="/clients", tags=["clients"])

# # Crear cliente
# @router.post("/", response_model=Client)
# def create_client(client: ClientCreate, db: Session = Depends(get_db)):
#     return crud.create_client(db=db, client=client)

# # Leer clientes
# @router.get("/", response_model=List[Client])
# def read_clients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     return crud.get_clients(db, skip=skip, limit=limit)

# # Leer cliente por ID
# @router.get("/{client_id}", response_model=Client)
# def read_client(client_id: int, db: Session = Depends(get_db)):
#     db_client = crud.get_client(db, client_id=client_id)
#     if db_client is None:
#         raise HTTPException(status_code=404, detail="Client not found")
#     return db_client

# # Actualizar cliente
# @router.put("/{client_id}", response_model=Client)
# def update_client(client_id: int, client: ClientCreate, db: Session = Depends(get_db)):
#     db_client = crud.update_client(db, client_id=client_id, client_data=client)
#     if db_client is None:
#         raise HTTPException(status_code=404, detail="Client not found")
#     return db_client

# # Eliminar cliente
# @router.delete("/{client_id}")
# def delete_client(client_id: int, db: Session = Depends(get_db)):
#     db_client = crud.delete_client(db, client_id=client_id)
#     if db_client is None:
#         raise HTTPException(status_code=404, detail="Client not found")
#     return {"detail": "Client deleted"}
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud
from app.schemas.client import Client, ClientCreate
from app.database import get_db

router = APIRouter(prefix="/v1/client", tags=["client"])

# Crear cliente (caut)
@router.post("/caut", response_model=Client)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    return crud.create_client(db=db, client=client)

# Obtener todos los clientes (gaut)
@router.get("/gaut", response_model=List[Client])
def read_clients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_clients(db, skip=skip, limit=limit)

# Obtener cliente por ID (gaut/{client_id})
@router.get("/gaut/{client_id}", response_model=Client)
def read_client(client_id: int, db: Session = Depends(get_db)):
    db_client = crud.get_client(db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client

# Actualizar cliente (uaut/{client_id})
@router.put("/uaut/{client_id}", response_model=Client)
def update_client(client_id: int, client: ClientCreate, db: Session = Depends(get_db)):
    db_client = crud.update_client(db, client_id=client_id, client_data=client)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client

# Eliminar cliente (daut/{client_id})
@router.delete("/daut/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_db)):
    db_client = crud.delete_client(db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return {"message": "Client deleted successfully"}
