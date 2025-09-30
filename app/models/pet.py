from sqlalchemy import Column, Integer, String, Date, ForeignKey
from ..database import Base

#tabla de mascotas

class Pet(Base):
    __tablename__="pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)                 # Nombre de la mascota
    especie = Column(String(50), nullable=False)               # Especie (perro, gato, etc.)
    raza = Column(String(100), nullable=True)                  # Raza
    sexo = Column(String(20), nullable=True)                   # Sexo
    nacimiento = Column(Date, nullable=True)                   # Fecha de nacimiento
    caracteristicas = Column(String(255), nullable=True)       # Características físicas
    dueno = Column(String(100), nullable=False)                # Dueño (texto por ahora)
    foto = Column(String(255), nullable=True) 
