from src.infra_postgre.repositorio.pessoas_repositorio import InserirPessoa
from src.use_cases.case_inserir_pessoa import Registrarpessoa
from src.presenters.conrollers.registrar_pessoa import RegisterPessoaController
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from faker import Faker
from src.models.pessoa_models import Pessoa
import unittest
from unittest.mock import patch, MagicMock
from src.infra_postgre.configs.connection.connection_db import conectar_db

faker = Faker()


class TestcontrollerPessoa(unittest.TestCase):

    @patch('src.infra_postgre.configs.connection.fechar_conexao')
    @patch('src.infra_postgre.configs.connection.connection_db')
    def setUp(self, mock_conectar_db, mock_fechar_conexao):
        # Mockar a conexão com o banco de dados
        self.mock_connection = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_conectar_db = mock_conectar_db
        self.mock_fechar_conexao = mock_fechar_conexao

        # Configurar o retorno dos mocks
        self.mock_conectar_db.return_value = {'connection': self.mock_connection, 'connection_pool': MagicMock()}
        self.mock_connection.cursor.return_value = self.mock_cursor
        self.mock_cursor.lastrowid = 1

    def test_insertPessoaController(self):

          pessoarepositorio = InserirPessoa(self.mock_conectar_db)
          usecase = Registrarpessoa(pessoarepositorio)
          registercontroller = RegisterPessoaController(usecase)

          http_request = HttpRequest()

          pessoa = Pessoa(
              id=0,
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

          data = {'nome': pessoa.nome,
                  'data_nascimento': pessoa.data_nascimento,
                  'telefone': pessoa.telefone,
                  'email': pessoa.email,
                  'sexo': pessoa.sexo,
                  'estado': pessoa.estado,
                  'cidade': pessoa.cidade,
                  'bairro': pessoa.bairro,
                  'logradouro': pessoa.logradouro,
                  'numero': pessoa.numero,
                  'status': pessoa.status,
                  'complemento': pessoa.complemento}

          http_request.query = data
          http_request.body = None
          http_request.body = None

          response = registercontroller.route_insert(http_request=http_request)
          print(response)


    def test_select_controller(self):
        pessoarepositorio = InserirPessoa(self.mock_conectar_db)
        usecase = Registrarpessoa(pessoarepositorio)
        registercontroller = RegisterPessoaController(usecase)

        http_request = HttpRequest()

        response = registercontroller.route_select(http_request=http_request)

        print(response)


    def test_select_by_id_controller(self):

        pessoarepositorio = InserirPessoa(self.mock_conectar_db)
        usecase = Registrarpessoa(pessoarepositorio)
        registercontroller = RegisterPessoaController(usecase)

        http_request = HttpRequest()
        http_request.query = {'pessoa_id': 21}

        response = registercontroller.route_select_by_id(http_request=http_request)

        print(response.status_code, response.body)

    def test_update_controller(self):
        pessoarepositorio = InserirPessoa(self.mock_conectar_db)
        usecase = Registrarpessoa(pessoarepositorio)
        registercontroller = RegisterPessoaController(usecase)

        http_request = HttpRequest()

        pessoa = Pessoa(
            id=63,
            nome='teste_controller2',
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

        data = {'id': pessoa.id,
                'nome': pessoa.nome,
                'data_nascimento': pessoa.data_nascimento,
                'telefone': pessoa.telefone,
                'email': pessoa.email,
                'sexo': pessoa.sexo,
                'estado': pessoa.estado,
                'cidade': pessoa.cidade,
                'bairro': pessoa.bairro,
                'logradouro': pessoa.logradouro,
                'numero': pessoa.numero,
                'status': pessoa.status,
                'complemento': pessoa.complemento}

        http_request.query = data
        http_request.body = None
        http_request.body = None

        response = registercontroller.route_update(http_request=http_request)
        print(response)


    def test_delete_controller(self):

        pessoarepositorio = InserirPessoa(self.mock_conectar_db)
        usecase = Registrarpessoa(pessoarepositorio)
        registercontroller = RegisterPessoaController(usecase)

        http_request = HttpRequest()
        http_request.query = {'pessoa_id': 10}

        response = registercontroller.route_delete(http_request=http_request)

        print(response)

