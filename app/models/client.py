# Importamos las clases y tipos de datos de SQLAlchemy para definir columnas en la tabla
from sqlalchemy import Column, Integer, String, Text  

# Importamos la clase Base desde el archivo database.py 
# Base es la clase base que registra los modelos como tablas en la base de datos
from ..database import Base  


# Definimos la clase Client como un modelo de SQLAlchemy
# Hereda de Base para que SQLAlchemy lo reconozca como tabla
class Client(Base):
    # Nombre de la tabla en la base de datos
    __tablename__ = "clients"

    # Columna ID -> clave primaria de la tabla, tipo entero
    # primary_key=True: identifica de forma única cada fila
    # index=True: crea un índice para búsquedas más rápidas
    id = Column(Integer, primary_key=True, index=True)

    # Columna name -> almacena el nombre del cliente
    # String(255): hasta 255 caracteres
    # nullable=False: obligatorio (no puede ser nulo)
    name = Column(String(255), nullable=False)

    # Columna email -> correo del cliente
    # También obligatorio y con máximo 255 caracteres
    email = Column(String(255), nullable=False)

    # Columna telephone -> teléfono del cliente
    # String(50): máximo 50 caracteres
    # nullable=True: este campo puede estar vacío
    telephone = Column(String(50), nullable=True)

    # Columna address -> dirección del cliente
    # Texto hasta 255 caracteres, también opcional
    address = Column(String(255), nullable=True)

    # Columna city -> ciudad del cliente
    # Texto de hasta 100 caracteres, opcional
    city = Column(String(100), nullable=True)

    # Columna description -> descripción larga del cliente
    # Tipo Text permite almacenar mucho más texto que String
    # También opcional
    description = Column(Text, nullable=True)
