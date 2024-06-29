from unittest.mock import patch, MagicMock
from faker import Faker
from src.infra_postgre.repositorio.pessoas_repositorio import InserirPessoa

faker = Faker()


@patch('src.infra_postgre.configs.connection.connection_db.conectar_db')
@patch('src.infra_postgre.configs.connection.fechar_conexao_db')
def test_inserir_pessoa(mock_fechar_conexao_db, mock_conectar_db):
    # Configuração do mock para conectar_db
    mock_connection = MagicMock()
    mock_cursor = MagicMock()
    mock_connection.cursor.return_value = mock_cursor
    mock_conectar_db.return_value = {'connection': mock_connection, 'connection_pool': MagicMock()}

    # Simulação de comportamento do cursor
    mock_cursor.fetchone.return_value = {'id': 1}

    pessoa = InserirPessoa()

    nome = 'aluísio'
    data_nascimento = str(faker.random_number(digits=8))
    telefone = faker.phone_number()
    email = faker.email()
    sexo = 'feminino'
    estado = faker.state()
    cidade = faker.city()
    bairro = faker.street_name()
    logradouro = faker.street_address()
    numero = '235'
    complemento = 'complemento'
    status = True

    response = pessoa.criar_pessoa(
        nome, data_nascimento, telefone,
        email, sexo, estado, cidade, bairro, logradouro, numero, status, complemento
    )

    # Verificações usando mocks
    #mock_conectar_db.assert_called_once()
    #mock_cursor.execute.assert_called_once()
    #mock_cursor.fetchone.assert_called_once()
    #mock_connection.commit.assert_called_once()
    #mock_fechar_conexao_db.assert_called_once_with(cursor=mock_cursor, connection=mock_connection, connection_pool=mock_conectar_db.return_value['connection_pool'])

    # Verificações de resultado
    assert response['nome'] == nome
    assert response['data_nascimento'] == data_nascimento
    assert response['telefone'] == telefone
    assert response['email'] == email
    assert response['sexo'] == sexo
    assert response['estado'] == estado
    assert response['cidade'] == cidade
    assert response['bairro'] == bairro
    assert response['logradouro'] == logradouro
    assert response['numero'] == numero
    assert response['complemento'] == complemento
    assert response['status'] == status

    print('Teste unitário de inserção de pessoa OK')

