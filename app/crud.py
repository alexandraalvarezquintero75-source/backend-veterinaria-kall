from sqlalchemy.orm import Session
from app.models.client import Client as ClientModel
from app.schemas.client import ClientCreate

# Crear cliente
def create_client(db: Session, client: ClientCreate):
    db_client = ClientModel(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

# Leer lista de clientes
def get_clients(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ClientModel).offset(skip).limit(limit).all()

# Leer cliente por ID
def get_client(db: Session, client_id: int):
    return db.query(ClientModel).filter(ClientModel.id == client_id).first()

# Eliminar cliente
def delete_client(db: Session, client_id: int):
    client = db.query(ClientModel).filter(ClientModel.id == client_id).first()
    if client:
        db.delete(client)
        db.commit()
    return client

# Actualizar cliente
def update_client(db: Session, client_id: int, client_data: ClientCreate):
    client = db.query(ClientModel).filter(ClientModel.id == client_id).first()
    if client:
        for key, value in client_data.dict().items():
            setattr(client, key, value)
        db.commit()
        db.refresh(client)
    return client
