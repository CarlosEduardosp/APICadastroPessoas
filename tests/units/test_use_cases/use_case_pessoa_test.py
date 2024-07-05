import datetime
from src.models.pessoa_models import Pessoa
from src.infra_postgre.repositorio.pessoas_repositorio import InserirPessoa
from src.use_cases.case_inserir_pessoa import Registrarpessoa
from faker import Faker
from src.infra_postgre.configs.connection.connection_db import conectar_db
from unittest.mock import patch, MagicMock
import unittest
from PIL import Image
import io


faker = Faker()


class TestUseCasePessoa(unittest.TestCase):

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

    def test_inserir_use_case(self):
        """ testes use case """

        repository = InserirPessoa(self.mock_conectar_db)
        teste = Registrarpessoa(repository)

        dados = Pessoa(
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

        response = teste.inserirpessoa(
            dados
        )
        print(response)

    def test_select(self):
        """ selecting pessoas """

        repository = InserirPessoa(self.mock_conectar_db)
        teste = Registrarpessoa(repository)

        response = teste.select_pessoas()

        print(response)


    def test_select_by_id(self):

        repository = InserirPessoa(self.mock_conectar_db)
        teste = Registrarpessoa(repository)

        response = teste.select_by_id(pessoa_id=2)

        if response:
            print(response)


    def test_update_use_case(self):
        """ testes use case """

        # Teste rápidos
        repository = InserirPessoa(conectar_db)
        teste = Registrarpessoa(repository)

        dados_atualizados = Pessoa(
            id=0,
            nome=faker.name(),
            data_nascimento='14051986',
            telefone='22992239273',
            email='eu@carol',
            sexo='M',
            estado='RJ',
            cidade='Araruama',
            bairro='picada',
            logradouro='estrada de são vicente',
            numero='11',
            status=True,
            complemento='complemento'
        )

        response = teste.atualizar_dados(pessoa=dados_atualizados, pessoa_id=54)
        print(response)


    def test_delete_use_case(self):
        repository = InserirPessoa(self.mock_conectar_db)
        teste = Registrarpessoa(repository)

        teste.pessoa_repository.deletar_pessoa(pessoa_id=1)
