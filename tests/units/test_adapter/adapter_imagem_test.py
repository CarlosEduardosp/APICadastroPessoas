from src.main.composer.imagem_composer import RegisterImagemComposer
from src.main.adapter.adapter_imagem import AdapterImagem
from unittest.mock import patch, MagicMock
from faker import Faker
from PIL import Image
import io
import unittest

faker = Faker()


class testAdapterImagem(unittest.TestCase):

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
        self.composer = RegisterImagemComposer(self.mock_conectar_db)


    def test_insert_adapter(self):
        # salvando o caminho da imagem
        caminho_da_imagem = 'C:/Users/carol/Downloads/kadu.jpg'

        # Abrir a imagem
        imagem = Image.open(caminho_da_imagem)

        # Salvar a imagem em um objeto BytesIO
        dados_binarios_fake = io.BytesIO()
        imagem.save(dados_binarios_fake, format='JPEG')

        buscar = AdapterImagem(
            api_route=self.composer.register_imagem_composer(),
            data={
                "nome": 'testadapter',
                "id_pessoa": 20,
                "imagem": dados_binarios_fake.getvalue()
            },
        )
        response = buscar.insert_adapter()

        print(response)


    def test_select(self):

        buscar = AdapterImagem(
            api_route=self.composer.register_imagem_composer(),
            data={}
        )

        response = buscar.select_adapter()

        print(response)


    def test_select_by_id(self):

        buscar = AdapterImagem(
            api_route=self.composer.register_imagem_composer(),
            data={"id_pessoa": 20}
        )

        response = buscar.select_by_id_adapter()
        print(response)


    def test_delete_adapter(self):
        buscar = AdapterImagem(
            api_route=self.composer.register_imagem_composer(),
            data={
                'id_pessoa': 20
            }
        )

        response = buscar.delete_adapter()
        print(response)

