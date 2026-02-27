
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from db import SessionLocal
from models import User, Perfil
from schemas import UserCreate, UserResponse, PerfilCreate, PerfilResponse

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=UserResponse)
def criar_usuario(dados: UserCreate):
    db: Session = SessionLocal()
    try:
        usuario_existente = db.query(User).filter(User.email == dados.email).first()
        if usuario_existente:
            raise HTTPException(status_code=400, detail="Email já cadastrado")

        perfil_obj = None
        if dados.perfil:
            perfil_obj = Perfil(perfil_nome=dados.perfil.perfil_nome)
            db.add(perfil_obj)
            db.flush()  

        novo_usuario = User(
            nome=dados.nome,
            email=dados.email,
            senha=dados.senha,
            id_perfil=perfil_obj.id if perfil_obj else None
        )
        db.add(novo_usuario)
        db.commit()
        db.refresh(novo_usuario)
        if perfil_obj:
            db.refresh(perfil_obj)
        return novo_usuario
    finally:
        db.close()

@router.get("/", response_model=list[UserResponse])
def listar_usuarios():
    db: Session = SessionLocal()
    usuarios = db.query(User).all()
    for usuario in usuarios:
        _ = usuario.perfil
    db.close()
    return usuarios

@router.get("/{usuario_id}", response_model=UserResponse)
def buscar_usuario(usuario_id: int):
    db: Session = SessionLocal()
    usuario = db.query(User).filter(User.id == usuario_id).first()
    if usuario:
        _ = usuario.perfil
    db.close()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return usuario

@router.delete("/{usuario_id}")
def deletar_usuario(usuario_id: int):
    db: Session = SessionLocal()
    usuario = db.query(User).filter(User.id == usuario_id).first()

    if not usuario:
        db.close()
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    db.delete(usuario)
    db.commit()
    db.close()

    return {"mensagem": "Usuário removido com sucesso"}