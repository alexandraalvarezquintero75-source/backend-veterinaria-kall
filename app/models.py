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
    
