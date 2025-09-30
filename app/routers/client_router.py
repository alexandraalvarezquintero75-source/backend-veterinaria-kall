# Importamos APIRouter para crear un grupo de rutas (endpoints)
# Depends permite inyectar recursos como la sesión de DB automáticamente
# HTTPException permite devolver errores HTTP personalizados (como 404)
from fastapi import APIRouter, Depends, HTTPException

# Importamos Session de SQLAlchemy para conectarnos a la base de datos
from sqlalchemy.orm import Session

# Importamos List para indicar que vamos a devolver listas de objetos
from typing import List

# Importamos las funciones CRUD (crear, leer, actualizar, eliminar) que definimos en crud.py
from app import crud

# Importamos los schemas de Pydantic para validar los datos de entrada y salida
# Client -> se usa cuando devolvemos datos al usuario
# ClientCreate -> se usa cuando recibimos datos para crear o actualizar un cliente
from app.schemas.client import Client, ClientCreate

# Importamos get_db, que nos da una sesión de base de datos activa
from app.database import get_db

# -------------------------------------------------
# Creamos un router de FastAPI específico para clientes
# -------------------------------------------------
# Todas las rutas que definamos aquí comenzarán con /v1/client
# En la documentación de Swagger aparecerán agrupadas bajo la etiqueta "client"
router = APIRouter(prefix="/v1/client", tags=["client"])

# -------------------------------------------------
# Endpoint para crear un cliente
# -------------------------------------------------
@router.post("/caut", response_model=Client)  # response_model valida la respuesta
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    """
    Recibe los datos de un cliente y los guarda en la base de datos.
    - client: datos que envía el usuario (nombre, email, etc.)
    - db: sesión de la base de datos que FastAPI inyecta automáticamente
    """
    # Llamamos a la función CRUD para crear el cliente y devolver el registro creado
    return crud.create_client(db=db, client=client)

# -------------------------------------------------
# Endpoint para obtener todos los clientes
# -------------------------------------------------
@router.get("/gaut", response_model=List[Client])  # devuelve lista de clientes
def read_clients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Obtiene todos los clientes de la base de datos con paginación.
    - skip: cuántos registros saltar (útil para paginar)
    - limit: cuántos registros devolver
    """
    # Llamamos a la función CRUD que devuelve los clientes de la DB
    return crud.get_clients(db, skip=skip, limit=limit)

# -------------------------------------------------
# Endpoint para obtener un cliente por su ID
# -------------------------------------------------
@router.get("/gaut/{client_id}", response_model=Client)  # devuelve un cliente
def read_client(client_id: int, db: Session = Depends(get_db)):
    """
    Busca un cliente específico por su ID.
    """
    # Llamamos a la función CRUD que busca el cliente en la DB
    db_client = crud.get_client(db, client_id=client_id)
    # Si no existe, devolvemos un error 404 al usuario
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    # Si existe, devolvemos los datos del cliente
    return db_client

# -------------------------------------------------
# Endpoint para actualizar un cliente
# -------------------------------------------------
@router.put("/uaut/{client_id}", response_model=Client)  # valida la salida
def update_client(client_id: int, client: ClientCreate, db: Session = Depends(get_db)):
    """
    Actualiza los datos de un cliente existente.
    """
    # Llamamos a la función CRUD que actualiza los datos en la DB
    db_client = crud.update_client(db, client_id=client_id, client_data=client)
    # Si el cliente no existe, devolvemos error 404
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    # Si se actualizó correctamente, devolvemos el cliente actualizado
    return db_client

# -------------------------------------------------
# Endpoint para eliminar un cliente
# -------------------------------------------------
@router.delete("/daut/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_db)):
    """
    Elimina un cliente por su ID.
    """
    # Llamamos a la función CRUD que elimina el cliente de la DB
    db_client = crud.delete_client(db, client_id=client_id)
    # Si no existe, devolvemos error 404
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    # Si se eliminó correctamente, devolvemos un mensaje de confirmación
    return {"message": "Client deleted successfully"}

# -------------------------------------------------
# Resumen general del archivo:
# -------------------------------------------------
# Este archivo define todas las rutas (endpoints) para gestionar clientes:
# - POST /caut → crear cliente
# - GET /gaut → obtener lista de clientes
# - GET /gaut/{id} → obtener cliente por ID
# - PUT /uaut/{id} → actualizar cliente
# - DELETE /daut/{id} → eliminar cliente
# Cada endpoint usa las funciones CRUD para interactuar con la base de datos
# y valida automáticamente los datos de entrada/salida usando los schemas de Pydantic.
