import unittest
from unittest.mock import patch, MagicMock
from src.infra_postgre.repositorio.pessoas_repositorio import InserirPessoa
from src.models.pessoa_models import Pessoa
from src.infra_postgre.configs.connection.connection_db import conectar_db


class TestInserirPessoa(unittest.TestCase):

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

    def test_criar_pessoa(self):
        # Dados mockados para a criação da pessoa
        pessoa = Pessoa(
            id=1,
            nome="Kadu Silva",
            data_nascimento="14051986",
            telefone="22912365478",
            email="joao@example.com",
            sexo="M",
            estado="SP",
            cidade="São Paulo",
            bairro="Centro",
            logradouro="Rua A",
            numero="100",
            status=True,
            complemento="Apt 101"
        )

        # Criar uma instância da classe InserirPessoa com o banco mock
        repo = InserirPessoa(self.mock_conectar_db)

        # criar uma instância da classe com banco real
        #repo = InserirPessoa(conectar_db)

        response = repo.criar_pessoa(pessoa=pessoa)

        # Verificações
        self.mock_cursor.execute(
            "INSERT INTO pessoas (nome, data_nascimento, telefone, email, sexo, estado, cidade, bairro, "
            "logradouro, numero, status, complemento) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
                pessoa.nome,
                pessoa.data_nascimento,
                pessoa.telefone,
                pessoa.email,
                pessoa.sexo,
                pessoa.estado,
                pessoa.cidade,
                pessoa.bairro,
                pessoa.logradouro,
                pessoa.numero,
                pessoa.status,
                pessoa.complemento
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
        self.assertEqual(response['nome'], insert_values[0])
        self.assertEqual(response['data_nascimento'], insert_values[1])
        self.assertEqual(response['telefone'], insert_values[2])
        self.assertEqual(response['email'], insert_values[3])
        self.assertEqual(response['sexo'], insert_values[4])
        self.assertEqual(response['estado'], insert_values[5])
        self.assertEqual(response['cidade'], insert_values[6])
        self.assertEqual(response['bairro'], insert_values[7])
        self.assertEqual(response['logradouro'], insert_values[8])
        self.assertEqual(response['numero'], insert_values[9])
        self.assertEqual(response['status'], insert_values[10])
        self.assertEqual(response['complemento'], insert_values[11])

        # Resultado dos testes
        print('Resultado teste repositorio', response)

    def test_select_all(self):
        # Criar uma instância da classe InserirPessoa com o banco mock
        repo = InserirPessoa(self.mock_conectar_db)

        # criar uma instância da classe com banco real
        #repo = InserirPessoa(conectar_db)

        response = repo.listar_pessoas()

        # Verificações
        self.mock_cursor.execute("SELECT * FROM pessoas;")
        self.mock_connection.commit()

        # Fechando conexão com banco de dados
        self.mock_fechar_conexao(cursor=self.mock_cursor, connection=self.mock_connection,
                                 connection_pool=self.mock_conectar_db.return_value['connection_pool'])

        # Resultado dos testes
        print('Resultado teste repositorio', response)

    def test_select_por_id(self):
        # Criar uma instância da classe InserirPessoa com o banco mock
        repo = InserirPessoa(self.mock_conectar_db)

        # criar uma instância da classe com banco real
        #repo = InserirPessoa(conectar_db)

        pessoa_id = 50

        response = repo.encontrar_pessoa_por_id(pessoa_id=pessoa_id)

        # Verificações
        self.mock_cursor.execute("SELECT * FROM pessoas WHERE nome = %s;", (pessoa_id,))
        self.mock_connection.commit()

        # Fechando conexão com banco de dados
        self.mock_fechar_conexao(cursor=self.mock_cursor, connection=self.mock_connection,
                                 connection_pool=self.mock_conectar_db.return_value['connection_pool'])


        # Resultado dos testes
        print('Resultado teste repositorio', response)

    def test_select_por_name(self):

        # Criar uma instância da classe InserirPessoa com o banco mock
        #repo = InserirPessoa(self.mock_conectar_db)

        # criar uma instância da classe com banco real
        repo = InserirPessoa(conectar_db)

        # parâmetro precisa ser nome completo
        pessoa_nome = 'Kadu Silva'

        response = repo.encontrar_pessoa_por_nome(pessoa_nome=pessoa_nome)

        # Verificações
        self.mock_cursor.execute("SELECT * FROM pessoas WHERE nome = %s;", (pessoa_nome,))
        self.mock_connection.commit()

        # Fechando conexão com banco de dados
        self.mock_fechar_conexao(cursor=self.mock_cursor, connection=self.mock_connection,
                                 connection_pool=self.mock_conectar_db.return_value['connection_pool'])


        # Resultado dos testes
        print('Resultado teste repositorio', response)

    def test_delete(self):

        # Criar uma instância da classe InserirPessoa com o banco mock
        repo = InserirPessoa(self.mock_conectar_db)

        # criar uma instância da classe com banco real
        # repo = InserirPessoa(conectar_db)

        response = repo.deletar_pessoa(pessoa_id=1)

        pessoa_id = 1

        # Verificações
        self.mock_cursor.execute("DELETE FROM pessoas WHERE id = %s;", (pessoa_id,))
        self.mock_connection.commit()

        # Fechando conexão com banco de dados
        self.mock_fechar_conexao(cursor=self.mock_cursor, connection=self.mock_connection,
                                 connection_pool=self.mock_conectar_db.return_value['connection_pool'])

        # Resultado dos testes
        print('Resultado teste repositorio', response)

    def test_atualizar_pessoa(self):

        # Dados mockados para a criação da pessoa
        pessoa = Pessoa(
            id=54,
            nome="Carol Padilha",
            data_nascimento="14051986",
            telefone="22912365478",
            email="joao@example.com",
            sexo="M",
            estado="SP",
            cidade="São Paulo",
            bairro="Centro",
            logradouro="Rua A",
            numero="100",
            status=True,
            complemento="Apt 101"
        )

        # Criar uma instância da classe InserirPessoa com o banco mock
        #repo = InserirPessoa(self.mock_conectar_db)

        # criar uma instância da classe com banco real
        repo = InserirPessoa(conectar_db)

        response = repo.atualizar_pessoa(pessoa_id=pessoa.id, pessoa=pessoa)

        # Verificações
        self.mock_cursor.execute(
                "UPDATE pessoas SET "
                "nome = %s, "
                "data_nascimento = %s, "
                "telefone = %s, "
                "email = %s, "
                "sexo = %s, "
                "estado = %s, "
                "cidade = %s, "
                "bairro = %s, "
                "logradouro = %s, "
                "numero = %s, "
                "status = %s, "
                "complemento = %s "
                "WHERE id = %s",
                (
                    pessoa.nome,
                    pessoa.data_nascimento,
                    pessoa.telefone,
                    pessoa.email,
                    pessoa.sexo,
                    pessoa.estado,
                    pessoa.cidade,
                    pessoa.bairro,
                    pessoa.logradouro,
                    pessoa.numero,
                    pessoa.status,
                    pessoa.complemento,
                    pessoa.id
                )
            )
        self.mock_connection.commit()

        # Recuperar o último id salvo no banco mockado
        id_pessoa = self.mock_cursor.lastrowid

        # Acessar os argumentos passados para o execute
        insert_query, insert_values = self.mock_cursor.execute.call_args[0]

        # Fechando conexão com banco de dados
        self.mock_fechar_conexao(cursor=self.mock_cursor, connection=self.mock_connection, connection_pool=self.mock_conectar_db.return_value['connection_pool'])

        # Resultado dos testes
        print('Resultado teste repositorio', response)

