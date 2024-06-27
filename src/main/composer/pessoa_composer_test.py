from .pessoa_composer import register_pessoa_composer
from faker import Faker
from src.presenters.helpers.http_models import HttpRequest
faker = Faker()


def composer():

    pessoa = register_pessoa_composer()

    data = {
            "nome": faker.name(),
            "data_nascimento": str(faker.random_number(digits=8)),
            "telefone": faker.name(),
            "email": faker.email(),
            "sexo": faker.name(),
            "estado": faker.name(),
            "cidade": faker.name(),
            "bairro": faker.name(),
            "logradouro": faker.name(),
            "numero": faker.name(),
            "status": True,
            "imagem": faker.name()
        }

    pessoa.route_insert(http_request=HttpRequest(query=data))


def select():

    pessoa = register_pessoa_composer()

    response = pessoa.route_select(http_request=HttpRequest(query={}))

    print(response)


def select_by_id():

    pessoa = register_pessoa_composer()

    response = pessoa.route_select_by_id(http_request=HttpRequest(query={"pessoa_id": 2}))

    print(response.body.nome)


def select_by_name():

    pessoa = register_pessoa_composer()

    response = pessoa.route_select_by_id(http_request=HttpRequest(query={"nome": 'Shannon Hernandez'}))

    print(response)


def test_update_composer():

    pessoa = register_pessoa_composer()

    data = {
            "nome": faker.name(),
            "data_nascimento": str(faker.random_number(digits=8)),
            "telefone": faker.name(),
            "email": faker.email(),
            "sexo": faker.name(),
            "estado": faker.name(),
            "cidade": faker.name(),
            "bairro": faker.name(),
            "logradouro": faker.name(),
            "numero": faker.name(),
            "status": True,
            "imagem": faker.name(),
            'id': 2
        }

    response = pessoa.route_update(http_request=HttpRequest(query=data))

    print(response)

