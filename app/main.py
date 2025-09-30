# Importamos FastAPI para crear la aplicación
# Depends permite inyectar recursos como la sesión de DB
# HTTPException permite devolver errores HTTP
from fastapi import FastAPI, Depends, HTTPException

# Importamos List para declarar que vamos a devolver listas de objetos
from typing import List

# Importamos Session de SQLAlchemy para conectarnos a la base de datos
from sqlalchemy.orm import Session

# Importamos CORSMiddleware para permitir que nuestro frontend haga peticiones al backend
from fastapi.middleware.cors import CORSMiddleware

# Importamos nuestros archivos de modelos, esquemas y funciones CRUD
from . import models, schemas, crud

# Importamos la configuración de la base de datos
from .database import SessionLocal, engine, Base

# Importamos los routers que contienen los endpoints (rutas) de clientes y mascotas
from app.routers import client_router 
from app.routers import pet_router
# from app.routers import client  # esta línea está comentada, no se usa

# ----------------------------
# Crear todas las tablas en la base de datos
# ----------------------------
# Esto revisa los modelos (Base) y crea las tablas si no existen
Base.metadata.create_all(bind=engine)

# ----------------------------
# Crear la aplicación FastAPI
# ----------------------------
app = FastAPI(title="Clients API")  # Le damos un nombre a la aplicación

# ----------------------------
# Configurar los orígenes permitidos para CORS
# ----------------------------
# Esto permite que el frontend (que corre en diferentes puertos) pueda hacer peticiones al backend
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5174",
    "http://localhost:5175",
    "http://127.0.0.1:5175",
]

# Agregamos el middleware de CORS a la aplicación
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # permite solo estos orígenes
    allow_credentials=True,       # permite enviar cookies/autenticación
    allow_methods=["*"],          # permite todos los métodos (GET, POST, PUT, DELETE)
    allow_headers=["*"],          # permite cualquier encabezado HTTP
)

# ----------------------------
# Función para manejar la sesión de base de datos
# ----------------------------
def get_db():
    """
    Crea una sesión de base de datos para usar en los endpoints
    y la cierra automáticamente cuando termina.
    """
    db = SessionLocal()  # abre una sesión
    try:
        yield db          # entrega la sesión al endpoint
    finally:
        db.close()        # cierra la sesión

# ----------------------------
# Incluir los routers en la aplicación
# ----------------------------
# Esto añade los endpoints definidos en cada router al backend
app.include_router(client_router.router)
app.include_router(pet_router.router)

# ----------------------------
# Resumen general:
# ----------------------------
# Este archivo es el punto de entrada principal de la aplicación FastAPI.
# Aquí se realiza:
# - Creación de las tablas en la base de datos (Base.metadata.create_all)
# - Configuración de FastAPI (título de la app, middlewares, etc.)
# - Configuración de CORS para permitir peticiones desde el frontend
# - Función get_db() para manejar la sesión con la base de datos
# - Inclusión de los routers (client_router y pet_router) que definen los endpoints
