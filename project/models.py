from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class Perfil(Base):
    __tablename__ = "perfis"

    id = Column(Integer, primary_key=True, index=True)
    perfil_nome = Column(String, nullable=False)
    usuario = relationship("User", back_populates="perfil", uselist=False)


class User(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    id_perfil = Column(Integer, ForeignKey("perfis.id"), unique=True)
    perfil = relationship("Perfil", back_populates="usuario", uselist=False)