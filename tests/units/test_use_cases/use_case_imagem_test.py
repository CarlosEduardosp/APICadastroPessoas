from src.use_cases.case_imagem import Registrarimagem
from faker import Faker
import unittest
from PIL import Image
import io
from unittest.mock import patch, MagicMock
from src.infra_postgre.configs.connection.connection_db import conectar_db
from src.infra_postgre.repositorio.imagem_repositorio import InserirImagem
import psycopg2
from src.models.imagem_models import Imagem

faker = Faker()


class TestUseCaseImagem(unittest.TestCase):

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

        # Teste rápidos
        repository = InserirImagem(self.mock_conectar_db)
        teste = Registrarimagem(repository)

        # salvando o caminho da imagem
        caminho_da_imagem = 'C:/Users/carol/Downloads/kadu.jpg'

        # Abrir a imagem
        imagem = Image.open(caminho_da_imagem)

        # Salvar a imagem em um objeto BytesIO
        dados_binarios_fake = io.BytesIO()
        imagem.save(dados_binarios_fake, format='JPEG')

        # Converter os dados binários para o tipo bytea
        dados_bytea = psycopg2.Binary(dados_binarios_fake.getvalue())

        dados = Imagem(id_imagem=0, id_pessoa=1, nome='testando_usecase', imagem=dados_bytea)

        teste.inseririmagem(dados)
        print('inserido')


    def test_select(self):
        """ selecting pessoas """

        repository = InserirImagem(self.mock_conectar_db)
        teste = Registrarimagem(repository)

        response = teste.select_imagem()

        print(response)


    def test_select_by_id(self):
        repository = InserirImagem(self.mock_conectar_db)
        teste = Registrarimagem(repository)

        response = teste.select_by_id_imagem(id_pessoa=12)

        if response:
            print(response)


    def test_delete_use_case(self):
        repository = InserirImagem(self.mock_conectar_db)
        teste = Registrarimagem(repository)

        teste.delete_imagem(id_pessoa=12)
