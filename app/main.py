from fastapi import FastAPI

import os

from api.endpoints import router
from core.database import engine
from core.models import Base

db_dir = "./db"
if os.path.exists(db_dir):
    os.mkdir(db_dir)

# Cria as tabelas do banco de dados na inicialização da aplicação
Base.metadata.create_all(engine)

app = FastAPI()

@app.get("/")
def hello_world():
    return {"Hello": "World"}

app.include_router(router)
