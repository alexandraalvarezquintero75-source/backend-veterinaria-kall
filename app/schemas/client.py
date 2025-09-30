# from pydantic import BaseModel

# class ClientCreate(BaseModel):
#     name: str
#     email: str
#     telephone: str | None = None
#     address: str | None = None
#     city: str | None = None
#     description: str | None = None

# class ClientResponse(BaseModel):
#     id: int
#     name: str
#     email: str
#     telephone: str | None = None
#     address: str | None = None
#     city: str | None = None
#     description: str | None = None

#     class Config:
# #         orm_mode = True  # Importante para devolver objetos SQLAlchemy
# from pydantic import BaseModel, EmailStr
# from typing import Optional

# class ClientBase(BaseModel):
#     name: str
#     email: EmailStr
#     telephone: Optional[str] = None
#     address: Optional[str] = None
#     city: Optional[str] = None
#     description: Optional[str] = None

# class ClientCreate(ClientBase):
#     pass

# class Client(ClientBase):
#     id: int

#     class Config:
#         from_attributes = True  # en lugar de orm_mode en Pydantic v2
from pydantic import BaseModel

# Esquema base (compartido entre Create y Client completo)
class ClientBase(BaseModel):
    name: str
    email: str
    telephone: str | None = None
    address: str | None = None
    city: str | None = None
    description: str | None = None

# Para crear cliente (request body)
class ClientCreate(ClientBase):
    pass

# Para leer cliente (response body)
class Client(ClientBase):
    id: int

    class Config:
        from_attributes = True  # En Pydantic v2 (antes era orm_mode = True)

