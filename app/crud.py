# Importamos Session de SQLAlchemy, que permite conectarnos y trabajar con la base de datos
from sqlalchemy.orm import Session

# Importamos el modelo Client de la base de datos (la tabla Client)
from app.models.client import Client as ClientModel

# Importamos el esquema ClientCreate de Pydantic para recibir datos de creación/actualización
from app.schemas.client import ClientCreate

# ---------------------------
# Crear cliente
# ---------------------------
def create_client(db: Session, client: ClientCreate):
    """
    Crea un nuevo cliente en la base de datos.
    """
    # Creamos un objeto ClientModel usando los datos que recibimos
    db_client = ClientModel(**client.dict())  
    # Lo agregamos a la sesión de la base de datos
    db.add(db_client)
    # Guardamos los cambios en la base de datos
    db.commit()
    # Refrescamos el objeto para obtener valores generados automáticamente, como el ID
    db.refresh(db_client)
    # Devolvemos el cliente creado
    return db_client

# ---------------------------
# Leer lista de clientes
# ---------------------------
def get_clients(db: Session, skip: int = 0, limit: int = 10):
    """
    Devuelve una lista de clientes de la base de datos con paginación.
    - skip: cuántos registros saltar
    - limit: cuántos registros devolver
    """
    # Consulta sobre ClientModel aplicando paginación
    return db.query(ClientModel).offset(skip).limit(limit).all()

# ---------------------------
# Leer cliente por ID
# ---------------------------
def get_client(db: Session, client_id: int):
    """
    Busca y devuelve un cliente por su ID.
    - Si no existe, devuelve None
    """
    return db.query(ClientModel).filter(ClientModel.id == client_id).first()

# ---------------------------
# Eliminar cliente
# ---------------------------
def delete_client(db: Session, client_id: int):
    """
    Elimina un cliente por su ID.
    """
    # Buscamos el cliente en la base de datos
    client = db.query(ClientModel).filter(ClientModel.id == client_id).first()
    if client:
        # Si existe, lo eliminamos
        db.delete(client)
        db.commit()
    # Retorna el cliente eliminado, o None si no existía
    return client

# ---------------------------
# Actualizar cliente
# ---------------------------
def update_client(db: Session, client_id: int, client_data: ClientCreate):
    """
    Actualiza los datos de un cliente existente.
    """
    # Buscamos cliente por ID
    client = db.query(ClientModel).filter(ClientModel.id == client_id).first()
    if client:
        # Recorremos los datos recibidos y actualizamos el cliente
        for key, value in client_data.dict().items():
            setattr(client, key, value)  # setattr cambia el valor del atributo
        # Guardamos los cambios en la base de datos
        db.commit()
        # Refrescamos el objeto para obtener los valores actualizados
        db.refresh(client)
    # Retorna el cliente actualizado, o None si no existía
    return client

# ---------------------------
# Resumen general:
# ---------------------------
# Este archivo implementa las funciones CRUD para el modelo Client:
# - create_client -> crea un nuevo cliente
# - get_clients   -> devuelve una lista de clientes (con paginación)
# - get_client    -> devuelve un cliente por su ID
# - update_client -> actualiza los datos de un cliente existente
# - delete_client -> elimina un cliente por ID
# Estas funciones son usadas por los endpoints del router de clientes
