from src.infra_postgre.repositorio.pessoas_repositorio import InserirPessoa
from src.use_cases.case_inserir_pessoa import Registrarpessoa
from src.presenters.conrollers.registrar_pessoa import RegisterPessoaController
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from faker import Faker
from PIL import Image
import io

faker = Faker()


def test_insertPessoaController():

      pessoarepositorio = InserirPessoa()
      usecase = Registrarpessoa(pessoarepositorio)
      registercontroller = RegisterPessoaController(usecase)

      http_request = HttpRequest()

      data = {'nome': faker.name(),
        'data_nascimento': str(14051990),
        'telefone': '22992239273',
        'email':faker.email(),
        'sexo':'M',
        'estado':faker.name(),
        'cidade':faker.name(),
        'bairro':faker.name(),
        'logradouro':faker.name(),
        'numero':'20',
        'status':True,
        'complemento': 'complemento'}

      http_request.query = data
      http_request.body = None
      http_request.body = None

      response = registercontroller.route_insert(http_request=http_request)
      print(response)


def test_select_controller():
    pessoarepositorio = InserirPessoa()
    usecase = Registrarpessoa(pessoarepositorio)
    registercontroller = RegisterPessoaController(usecase)

    http_request = HttpRequest()

    response = registercontroller.route_select(http_request=http_request)

    print(response)


def test_select_by_id_controller():

    pessoarepositorio = InserirPessoa()
    usecase = Registrarpessoa(pessoarepositorio)
    registercontroller = RegisterPessoaController(usecase)

    http_request = HttpRequest()
    http_request.query = {'pessoa_id': 21}

    response = registercontroller.route_select_by_id(http_request=http_request)

    print(response.status_code, response.body)


def select_by_name_controller():

    pessoarepositorio = InserirPessoa()
    usecase = Registrarpessoa(pessoarepositorio)
    registercontroller = RegisterPessoaController(usecase)

    http_request = HttpRequest()
    http_request.query = {'nome': 'Valerie Green'}

    response = registercontroller.route_select_by_name(http_request=http_request)

    print(response.status_code, response.body)


def test_update_controller():
    pessoarepositorio = InserirPessoa()
    usecase = Registrarpessoa(pessoarepositorio)
    registercontroller = RegisterPessoaController(usecase)

    http_request = HttpRequest()

    data = {'nome': 'kadu',
            'data_nascimento': '14051980',
            'telefone': faker.name(),
            'email': faker.email(),
            'sexo': 'feminino',
            'estado': faker.name(),
            'cidade': faker.name(),
            'bairro': faker.name(),
            'logradouro': faker.name(),
            'numero': '32',
            'status': True,
            'complemento': 'complemento',
            'id': 21}

    http_request.query = data
    http_request.body = None
    http_request.body = None

    response = registercontroller.route_update(http_request=http_request)
    print(response)


def test_delete_controller():

    pessoarepositorio = InserirPessoa()
    usecase = Registrarpessoa(pessoarepositorio)
    registercontroller = RegisterPessoaController(usecase)

    http_request = HttpRequest()
    http_request.query = {'pessoa_id': 22}

    response = registercontroller.route_delete(http_request=http_request)

    print(response)

