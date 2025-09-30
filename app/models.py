from sqlalchemy import Column, Integer, String, Float
from .database import Base
# Aqui defino las columnas que queremos en la base de datos
# Aquí se crean todas las tablas de la base de datos
class Product(Base):
    __tablename__ = "products"  #nombre de la tabla en mysql

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    
class Client(Base):
    __tablename__ = "clients"  #nombre de la tabla en mysql

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    
# Este archivo define los modelos ORM (tablas) usando SQLAlchemy.
# Cada clase representa una tabla en la base de datos:
# - Product: tabla "products" con columnas id, name y price
# - Client: tabla "clients" con columnas id, full_name y email
# Estos modelos se usan en crud.py para interactuar con la base de datos.