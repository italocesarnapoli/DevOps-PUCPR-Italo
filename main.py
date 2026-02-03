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

async def listar_tarefas():
    tarefa_nova = Tarefa(id=0, titulo="nova tarefa", data_criacao=datetime.now(), finalizado=False)
    return tarefa_nova

API.add_api_route("/tarefas", listar_tarefas, methods=['GET'])