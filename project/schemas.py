from pydantic import BaseModel
from typing import Optional

class PerfilCreate(BaseModel):
    perfil_nome: str

class PerfilResponse(BaseModel):
    id: int
    perfil_nome: str

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    nome: str
    email: str
    senha: str
    perfil: Optional[PerfilCreate] = None

class UserResponse(BaseModel):
    id: int
    nome: str
    email: str
    id_perfil: Optional[int] = None
    perfil: Optional[PerfilResponse] = None

    class Config:
        from_attributes = True