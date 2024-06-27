import datetime
from src.infra_postgre.repositorio.pessoas_repositorio import InserirPessoa
from src.use_cases.case_inserir_pessoa import Registrarpessoa
from faker import Faker
from PIL import Image
import io

faker = Faker()


def test_inserir_use_case():
    """ testes use case """

    repository = InserirPessoa()
    teste = Registrarpessoa(repository)

    response = teste.inserirpessoa(
        nome=faker.name(),
        data_nascimento=str(faker.random_number(digits=8)),
        telefone=faker.name(),
        email=faker.email(),
        sexo='masculino',
        estado=faker.name(),
        cidade=faker.name(),
        bairro=faker.name(),
        logradouro=faker.name(),
        numero='25',
        status=True,
        complemento=faker.name()
    )
    print(response)

def test_select():
    """ selecting pessoas """

    repository = InserirPessoa()
    teste = Registrarpessoa(repository)

    response = teste.select_pessoas()

    print(response)


def test_select_by_id():

    repository = InserirPessoa()
    teste = Registrarpessoa(repository)

    response = teste.select_by_id(pessoa_id=2)

    if response:
        print(response)


def test_select_by_nome():
    repository = InserirPessoa()
    teste = Registrarpessoa(repository)

    response = teste.select_by_nome(nome='kadu')

    if response:
        print(response)


def test_update_use_case():
    """ testes use case """

    # Teste rápidos
    repository = InserirPessoa()
    teste = Registrarpessoa(repository)

    dados_atualizados = {
        'nome': 'Caroline',
        'data_nascimento': '14051986',
        'telefone': '22992239273',
        'email': 'eu@carol',
        'sexo': 'M',
        'estado': 'RJ',
        'cidade': 'Araruama',
        'bairro': 'picada',
        'logradouro': 'estrada de são vicente',
        'numero': '11',
        'status': True,
        'complemento': 'complemento'
    }
    response = teste.atualizar_dados(pessoa_id=1, dados_atualizados=dados_atualizados)
    print(response)


def test_delete_use_case():
    repository = InserirPessoa()
    teste = Registrarpessoa(repository)

    teste.pessoa_repository.deletar_pessoa(pessoa_id="1")
