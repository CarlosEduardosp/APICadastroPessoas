from faker import Faker
from src.infra_postgre.repositorio.pessoas_repositorio import InserirPessoa

faker = Faker()


def test_inserir_pessoa():
    pessoa = InserirPessoa()

    response = pessoa.criar_pessoa(
        nome=faker.name(),
        data_nascimento=str(faker.random_number(digits=8)),
        telefone=faker.name(),
        email=faker.email(),
        sexo=f'feminino',
        estado=faker.name(),
        cidade=faker.name(),
        bairro=faker.name(),
        logradouro=faker.name(),
        numero='235',
        complemento=faker.name(),
        status=True
    )

    print(response)


def test_select_todos():
    pessoa = InserirPessoa()

    response = pessoa.listar_pessoas()

    print(response)


def test_select_pessoa_id():
    pessoa = InserirPessoa()

    response = pessoa.encontrar_pessoa_por_id(pessoa_id=1)

    print(response)


def test_deletar():
    pessoa = InserirPessoa()

    response = pessoa.deletar_pessoa(pessoa_id=3)

    print(response)


def test_update():
    pessoa = InserirPessoa()

    pessoa_id = 1

    dados_atualizados = {
        'nome': faker.name(),
        'data_nascimento': faker.name(),
        'telefone': faker.name(),
        'email': faker.email(),
        'sexo': 'm',
        'estado': faker.name(),
        'cidade': faker.name(),
        'bairro': faker.name(),
        'logradouro': faker.name(),
        'numero': '238',
        'complemento': faker.name(),
        'status': True
    }

    response = pessoa.atualizar_pessoa(
        pessoa_id=pessoa_id,
        dados_atualizados=dados_atualizados
    )

    print(response)
