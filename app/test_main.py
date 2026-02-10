from .main import API

from fastapi.testclient import TestClient

CLIENT = TestClient(API)

def testar_endpoint_tarefas():
    requisicao = CLIENT.get("/tarefas")

    assert requisicao.status_code == 200

def testar_endpoint_criar_tarefa():
    requisicao = CLIENT.post("/criar", params={'titulo': 'teste'})

    assert requisicao.json() == {"mensagem": "OK"}

    requisicao = CLIENT.get('tarefas')

    assert len(requisicao.json()) == 1
    assert requisicao.json()[0]['id'] == 0