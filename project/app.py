from fastapi import FastAPI
from db import engine, Base
import user_routes

app = FastAPI(title="Sistema de Usuários")

Base.metadata.create_all(bind=engine)

app.include_router(user_routes.router)