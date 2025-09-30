# Importamos BaseModel de Pydantic
# BaseModel nos permite definir "plantillas" de datos y validar que sean correctos
from pydantic import BaseModel

# ---------------------------------------------------
# Esquema base (lo que todos los clientes tienen)
# ---------------------------------------------------
class ClientBase(BaseModel):
    # Campos obligatorios (siempre deben venir)
    name: str          # Nombre del cliente
    email: str         # Correo electrónico del cliente

    # Campos opcionales (pueden venir o no)
    telephone: str | None = None   # Teléfono del cliente
    address: str | None = None     # Dirección
    city: str | None = None        # Ciudad
    description: str | None = None # Descripción adicional

# ---------------------------------------------------
# Esquema para CREAR cliente
# ---------------------------------------------------
class ClientCreate(ClientBase):
    # Este esquema se usa cuando enviamos datos para crear un cliente
    # Hereda todos los campos de ClientBase
    # No necesita nada más por ahora
    pass

# ---------------------------------------------------
# Esquema para LEER cliente (respuesta)
# ---------------------------------------------------
class Client(ClientBase):
    # Además de los campos de ClientBase, agregamos el id
    # porque cuando obtenemos datos de la DB siempre queremos saber su identificador
    id: int

    class Config:
        # Permite que Pydantic pueda trabajar con objetos de SQLAlchemy
        # Convierte automáticamente objetos de la DB en modelos Pydantic
        from_attributes = True

# ---------------------------------------------------
# Explicación general:
# - ClientBase: define los campos comunes que siempre tiene un cliente
# - ClientCreate: se usa cuando enviamos datos para crear o actualizar un cliente
# - Client: se usa cuando devolvemos datos al usuario (incluye id)
# FastAPI usa estos modelos para validar que los datos de entrada y salida sean correctos
