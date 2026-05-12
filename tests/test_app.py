from http import HTTPStatus

from fastapi.testclient import TestClient

from app.main import app


def test_app():
    # Cria um cliente de testes usando a aplicação como base
    # Arrange -> Organizar
    client = TestClient(app)

    # Faz uma requisição
    # Act -> Agir
    response = client.get("/")

    # Aqui faz a validação do código de resposta, para saber se a resposta é
    # referente ao código 200.
    # Assert -> Afirmar
    assert response.status_code == HTTPStatus.OK

    # Valida se o dicionário que enviamos na função é o mesmo que recebemos
    # quando faz a requisição.
    # Assert -> Afirmar
    assert response.json() == {"message": "Olá Mundo!"}
