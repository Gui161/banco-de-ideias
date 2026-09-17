from sqlalchemy import create_engine, Column, String, Integer, Float, ForeignKey, DateTime, JSON
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from data.data_base import base
from datetime import datetime

class Usuario(base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, default='usuario')
    papel = Column(String, nullable=False)
    senha = Column(String, nullable=False)
    
    ideias = relationship("Ideia", back_populates="usuario")

class Ideia(base):
    __tablename__ = "ideias"

    id = Column(Integer, primary_key=True, index=True)
    usuarios_id = Column(Integer, ForeignKey("usuarios.id"))
    titulo = Column(String, nullable=False)
    estagio = Column(Integer, default=1)
    pontos = Column(Integer, default=10)
    status = Column(String, default="Em análise")
    data_criacao = Column(DateTime, default=datetime.utcnow)
    conteudo = Column(JSON)

    usuario = relationship("Usuario", back_populates="ideias")