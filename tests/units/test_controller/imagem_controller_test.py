import unittest
from unittest.mock import patch, MagicMock
from src.infra_postgre.repositorio.imagem_repositorio import InserirImagem
from src.use_cases.case_imagem import Registrarimagem
from src.presenters.conrollers.registrar_imagem import RegisterImagemController
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from src.infra_postgre.configs.connection.connection_db import conectar_db
from faker import Faker
from PIL import Image
import io

faker = Faker()


class TestcontrollerImagem(unittest.TestCase):

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

          imagemrepositorio = InserirImagem(self.mock_conectar_db)
          usecase = Registrarimagem(imagemrepositorio)
          registercontroller = RegisterImagemController(usecase)

          http_request = HttpRequest()

          # salvando o caminho da imagem
          caminho_da_imagem = './imagem_para_teste/teste.jpg'

          # Abrir a imagem
          imagem = Image.open(caminho_da_imagem)

          # Salvar a imagem em um objeto BytesIO
          dados_binarios_fake = io.BytesIO()
          imagem.save(dados_binarios_fake, format='JPEG')

          data = {
            'nome': faker.name(),
            'id_pessoa': 10,
            'imagem': dados_binarios_fake.getvalue()}

          http_request.query = data
          http_request.body = None
          http_request.body = None

          response = registercontroller.route_insert_imagem(http_request=http_request)
          print(response)


    def test_select_controller(self):

        imagemrepositorio = InserirImagem(self.mock_conectar_db)
        usecase = Registrarimagem(imagemrepositorio)
        registercontroller = RegisterImagemController(usecase)

        http_request = HttpRequest()

        response = registercontroller.route_select(http_request=http_request)

        print(response)


    def test_select_by_id_controller(self):

        imagemrepositorio = InserirImagem(self.mock_conectar_db)
        usecase = Registrarimagem(imagemrepositorio)
        registercontroller = RegisterImagemController(usecase)

        http_request = HttpRequest()
        http_request.query = {'id_pessoa': 10}

        response = registercontroller.route_select_by_id(http_request=http_request)

        print(response.status_code, response.body)


    def test_delete_controller(self):

        imagemrepositorio = InserirImagem(self.mock_conectar_db)
        usecase = Registrarimagem(imagemrepositorio)
        registercontroller = RegisterImagemController(usecase)

        http_request = HttpRequest()
        http_request.query = {'id_pessoa': 1}

        response = registercontroller.route_delete(http_request=http_request)

        print(response)

