from http import HTTPStatus


def test_app(client):
    # Cria um cliente de testes usando a aplicação como base
    # Arrange -> Organizar

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


def test_create_user(client):
    dados_json = {
        "username": "HILSON DE OLIVEIRA SANTOS",
        "email": "hosantos@exemple.com",
        "password": "111424",
    }
    response = client.post("/api/v1/users/", json=dados_json)
    assert response.status_code == HTTPStatus.CREATED
    # assert response.json() == dados_json
    print(response.json())


def test_list_users(client):
    response = client.get("/api/v1/users/")
    assert response.status_code == HTTPStatus.OK
    print(response.json())


def test_update_user(client):
    dados_json = {
        "username": "HILSON DE OLIVEIRA SANTOS",
        "email": "hsantos@exemple.com",
        "password": "147528",
    }
    response = client.put("/api/v1/users/1", json=dados_json)
    assert response.status_code == HTTPStatus.OK
    # assert response.json() == dados_json
    print(response.json())


def test_delete_user(client):
    response = client.delete("/api/v1/users/1")
    assert response.status_code == HTTPStatus.OK
    print(response.json())
