from src.main.composer.pessoa_composer import RegisterPessoaComposer
from src.main.adapter.adapter_pessoa import AdapterPessoa
from src.infra_postgre.configs.connection.connection_db import conectar_db
from faker import Faker
from unittest.mock import patch, MagicMock
from PIL import Image
import io
import unittest


faker = Faker()


class testAdapterPessoa(unittest.TestCase):

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

        # composer para testes
        self.composer = RegisterPessoaComposer(self.mock_conectar_db)

    def test_insert_adapter(self):

        buscar = AdapterPessoa(
            api_route=self.composer.register_pessoa_composer(),
            data={
                "nome": 'testadapter',
                "data_nascimento": '14051986',
                "telefone": '63566663333',
                "email": faker.email(),
                "sexo": 'masculino',
                "estado": faker.name(),
                "cidade": faker.name(),
                "bairro": faker.name(),
                "logradouro": faker.name(),
                "numero": '890',
                "status": True,
                "complemento": 'complemento'
            },
        )
        response = buscar.insert_adapter()

        print(response)


    def test_select(self):

        buscar = AdapterPessoa(
            api_route=self.composer.register_pessoa_composer(),
            data={}
        )

        response = buscar.select_adapter()

        print(response)


    def test_select_by_id(self):

        buscar = AdapterPessoa(
            api_route=self.composer.register_pessoa_composer(),
            data={"pessoa_id": 24}
        )

        response = buscar.select_by_id_adapter()
        print(response)


    def test_update_adapter(self):
        buscar = AdapterPessoa(
            api_route=self.composer.register_pessoa_composer(),
            data={
                "nome": 'Caroline Padilha',
                "data_nascimento": '11111994',
                "telefone": '22658859669',
                "email": faker.email(),
                "sexo": 'feminino',
                "estado": faker.name(),
                "cidade": faker.name(),
                "bairro": faker.name(),
                "logradouro": faker.name(),
                "numero": '900',
                "status": True,
                "complemento": faker.name(),
                'id': 28
            },
        )
        response = buscar.update_adapter()

        print(response)


    def test_delete_adapter(self):
        buscar = AdapterPessoa(
            api_route=self.composer.register_pessoa_composer(),
            data={
                'pessoa_id':2
            }
        )

        response = buscar.delete_adapter()
        print(response)

