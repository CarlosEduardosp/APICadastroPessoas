import unittest
from PIL import Image
import io
from unittest.mock import patch, MagicMock
from src.infra_postgre.configs.connection.connection_db import conectar_db
from src.infra_postgre.repositorio.imagem_repositorio import InserirImagem
import psycopg2
from src.models.imagem_models import Imagem


class TestInserirImagem(unittest.TestCase):

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

    def test_inserir_imagem(self):

        # salvando o caminho da imagem
        caminho_da_imagem = './imagem_para_teste/teste.jpg'

        # Abrir a imagem
        imagem = Image.open(caminho_da_imagem)

        # Salvar a imagem em um objeto BytesIO
        dados_binarios_fake = io.BytesIO()
        imagem.save(dados_binarios_fake, format='JPEG')

        # Converter os dados binários para o tipo bytea
        dados_bytea = psycopg2.Binary(dados_binarios_fake.getvalue())

        # dados mockados
        dados_imagem = Imagem(
            id_imagem=0,
            id_pessoa=1,
            nome='teste_imagem',
            imagem=dados_bytea
        )

        # criar uma instância da classe com banco real
        #repo = InserirImagem(conectar_db)

        # criar uma instância da classe com banco mockado
        repo = InserirImagem(self.mock_conectar_db)

        response = repo.criar_imagem(dados_imagem)

        # Verificações
        self.mock_cursor.execute(
            "INSERT INTO imagem (id_pessoa, nome, imagem) VALUES (%s, %s, %s)",
            (
                dados_imagem.id_pessoa, dados_imagem.nome, dados_imagem.imagem
            )
        )
        self.mock_connection.commit()

        # Recuperar o último id salvo no banco mockado
        id_pessoa = self.mock_cursor.lastrowid

        # Acessar os argumentos passados para o execute
        insert_query, insert_values = self.mock_cursor.execute.call_args[0]

        # Fechando conexão com banco de dados
        self.mock_fechar_conexao(cursor=self.mock_cursor, connection=self.mock_connection, connection_pool=self.mock_conectar_db.return_value['connection_pool'])

        # Validações com assertEqual, realizando comparações entre os dados da função testada, com dados do mock

        # Resultado dos testes
        print('Resultado teste test_repositorio', response)

    def test_listar_imagens(self):

        # Criar uma instância da classe InserirPessoa com o banco mock
        repo = InserirImagem(self.mock_conectar_db)

        # criar uma instância da classe com banco real
        #repo = InserirImagem(conectar_db)

        response = repo.listar_imagens()

        # Verificações
        self.mock_cursor.execute("SELECT * FROM imagens;")
        self.mock_connection.commit()

        # Fechando conexão com banco de dados
        self.mock_fechar_conexao(cursor=self.mock_cursor, connection=self.mock_connection,
                                 connection_pool=self.mock_conectar_db.return_value['connection_pool'])

        # Resultado dos testes
        print('Resultado teste test_repositorio', response)

    def test_select_por_id(self):

        # Criar uma instância da classe InserirPessoa com o banco mock
        repo = InserirImagem(self.mock_conectar_db)

        # criar uma instância da classe com banco real
        #repo = InserirImagem(conectar_db)

        pessoa_id = 1

        response = repo.encontrar_imagem_por_id(id_pessoa=pessoa_id)

        # Verificações
        self.mock_cursor.execute("SELECT * FROM pessoas WHERE nome = %s;", (pessoa_id,))
        self.mock_connection.commit()

        # Fechando conexão com banco de dados
        self.mock_fechar_conexao(cursor=self.mock_cursor, connection=self.mock_connection,
                                 connection_pool=self.mock_conectar_db.return_value['connection_pool'])


        # Resultado dos testes
        print('Resultado teste test_repositorio', response)


    def test_delete(self):

        # Criar uma instância da classe InserirPessoa com o banco mock
        repo = InserirImagem(self.mock_conectar_db)

        # criar uma instância da classe com banco real
        #repo = InserirImagem(conectar_db)

        response = repo.deletar_imagem(id_pessoa=1)

        pessoa_id = 1

        # Verificações
        self.mock_cursor.execute("DELETE FROM pessoas WHERE id = %s;", (pessoa_id,))
        self.mock_connection.commit()

        # Fechando conexão com banco de dados
        self.mock_fechar_conexao(cursor=self.mock_cursor, connection=self.mock_connection,
                                 connection_pool=self.mock_conectar_db.return_value['connection_pool'])

        # Resultado dos testes
        print('Resultado teste test_repositorio', response)
