from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
# aqui definimos los endpoint
from . import models, schemas, crud
from .database import SessionLocal, engine, Base
from app.routers import client_router 
# from app.routers import client


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Clients API")

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5174",
    "http://localhost:5175",
    "http://127.0.0.1:5175",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(client_router.router)
# app.include_router(client.router)