# Importamos 'os' para poder leer datos de nuestro sistema, como usuario y contraseña
import os

# Importamos 'create_engine' para crear la conexión con la base de datos
from sqlalchemy import create_engine

# Importamos 'sessionmaker' para crear sesiones que nos permiten hablar con la base de datos
# Importamos 'declarative_base' para poder definir nuestras tablas como clases de Python
from sqlalchemy.orm import sessionmaker, declarative_base

# Importamos 'load_dotenv' para leer información guardada en un archivo .env
from dotenv import load_dotenv

# -----------------------------------------------------
# Preparar los datos para conectarnos a la base de datos
# -----------------------------------------------------

# Esto lee el archivo .env y carga los datos dentro del programa
load_dotenv()

# Leemos los datos de la base de datos desde el archivo .env
# Si no están, usamos valores por defecto
DB_USER = os.getenv("DB_USER", "root")        # Nombre de usuario
DB_PASS = os.getenv("DB_PASS", "password")    # Contraseña
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")   # Dirección del servidor
DB_PORT = os.getenv("DB_PORT", "3306")        # Puerto del servidor
DB_NAME = os.getenv("DB_NAME", "test_db")     # Nombre de la base de datos

# Creamos la "dirección completa" para conectarnos a la base de datos
# Esto le dice a SQLAlchemy cómo encontrar y entrar a la DB
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# -----------------------------------------------------
# Configurar SQLAlchemy para trabajar con la base de datos
# -----------------------------------------------------

# Creamos el "motor" que se encarga de hablar con la base de datos
# echo=True -> muestra en la consola todo lo que se hace (útil para revisar errores)
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)

# Creamos una "fábrica de sesiones" que nos permitirá abrir y cerrar conexiones a la DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para definir las tablas de la base de datos como clases de Python
Base = declarative_base()

# -----------------------------------------------------
# Función para usar la base de datos dentro de FastAPI
# -----------------------------------------------------
def get_db():
    """
    Esta función da una sesión de la base de datos para usar dentro de FastAPI.
    """
    db = SessionLocal()  # Abrimos una nueva sesión
    try:
        yield db          # Entregamos la sesión al endpoint
    finally:
        db.close()        # Cerramos la sesión cuando terminamos
