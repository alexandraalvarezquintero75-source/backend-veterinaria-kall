from sqlalchemy import Column, Integer, String, Text
from ..database import Base  #  conexión a la DB

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    telephone = Column(String(50), nullable=True)
    address = Column(String(255), nullable=True)
    city = Column(String(100), nullable=True)
    description = Column(Text, nullable=True)
