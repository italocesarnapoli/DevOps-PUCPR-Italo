from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

API = FastAPI()
TAREFAS = []

class Tarefa(BaseModel):
    id: int
    titulo: str
    data_criacao: datetime
    finalizado: bool = False

async def criar_tarefa(titulo: str):
    id = len(TAREFAS)
    tarefa_nova = Tarefa(id=id, titulo=titulo, data_criacao=datetime.now(), finalizado=False)

    TAREFAS.append(tarefa_nova)

    return {"mensagem": "OK"}

async def pagina_inicial():
    return {"mensagem": "Funcionando!"}

async def listar_tarefas():
    return TAREFAS

API.add_api_route("/tarefas", listar_tarefas, methods=['GET'])
API.add_api_route("/criar", criar_tarefa, methods=['POST'])
API.add_api_route("/", pagina_inicial, methods=['GET'])
