import unittest
from unittest.mock import patch, MagicMock
from src.infra_postgre.repositorio.pessoas_repositorio import InserirPessoa
from src.models.pessoa_models import Pessoa
from src.infra_postgre.configs.connection.connection_db import conectar_db


class TestInserirPessoa(unittest.TestCase):

    @patch('src.infra_postgre.configs.connection.connection_db')
    @patch('src.infra_postgre.configs.connection.fechar_conexao')
    def test_criar_pessoa(self, mock_fechar_conexao, mock_conectar_db):

        # Mockar a conexão com o banco de dados
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_conectar_db.return_value = {'connection': mock_connection, 'connection_pool': MagicMock()}
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.lastrowid = 1

        # Dados mockados para a criação da pessoa
        pessoa = Pessoa(
            id=10,
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

        # Criar uma instância da classe InserirPessoa
        repo = InserirPessoa(mock_conectar_db)  # banco mock
        #repo = InserirPessoa(conectar_db)  # banco real
        response = repo.criar_pessoa(pessoa=pessoa)

        # Verificações
        mock_cursor.execute(
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
                pessoa.complemento)
        )
        mock_connection.commit()

        # recupera o ultimo id salvo no banco mockado.
        id_pessoa = mock_cursor.lastrowid

        # Acessar os argumentos passados para o execute, insert_query == query executada,
        # insert_values == valores enviados
        insert_query, insert_values = mock_cursor.execute.call_args[0]

        #print("Query executada:", insert_query)
        #print("Valores enviados:", insert_values)

        # fechando conexão com banco de dados
        mock_fechar_conexao(cursor=mock_cursor, connection=mock_connection, connection_pool=mock_conectar_db.return_value['connection_pool'])

        # validações com assertEqual, realizando comparações entre os dados da função testada, com dados do mock.
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

        # resultado dos testes
        print('Resultado teste repositorio', response)

