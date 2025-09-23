from fastapi import FastAPI

from api.endpoints import router
from core.database import engine
from core.models import Base

# Cria as tabelas do banco de dados na inicialização da aplicação
Base.metadata.create_all(engine)

app = FastAPI()

@app.get("/")
def hello_world():
    return {"Hello": "World"}

app.include_router(router)
    