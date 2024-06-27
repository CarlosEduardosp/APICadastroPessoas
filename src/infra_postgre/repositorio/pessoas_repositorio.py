from src.infra_postgre.configs.connection.connection_db import conectar_db
from src.infra_postgre.configs.connection.fechar_conexao import fechar_conexao_db
from src.infra_postgre.repositorio.interfaces_repositorio.interface_repositorio import InterfacePessoaRepository
from psycopg2.extras import DictCursor


class InserirPessoa(InterfacePessoaRepository):

    def criar_pessoa(self, nome, data_nascimento, telefone, email, sexo, estado, cidade, bairro, logradouro, numero,
                     status, complemento):

        # conectando ao banco
        conn = conectar_db()
        connection = conn['connection']

        # criando um cursor
        cursor = connection.cursor(cursor_factory=DictCursor)

        cursor.execute(f"INSERT INTO pessoas(nome, data_nascimento, telefone, "
                       f"email, sexo, estado, cidade, bairro, logradouro, numero, status, complemento)"
                       f"VALUES('{nome}', '{data_nascimento}', '{telefone}',"
                       f"'{email}', '{sexo}', '{estado}', '{cidade}', '{bairro}', '{logradouro}', '{numero}', '{status}', '{complemento}')")

        # Recupere o ID gerado automaticamente
        cursor.execute("SELECT lastval() as id")
        id_pessoa = cursor.fetchone()['id']

        connection.commit()

        # fechando conexão com banco.
        fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])

        # Construa o objeto de resposta com os dados da pessoa e o ID
        response = {
            'id': id_pessoa,
            'nome': nome,
            'data_nascimento': data_nascimento,
            'telefone': telefone,
            'email': email,
            'sexo': sexo,
            'estado': estado,
            'cidade': cidade,
            'bairro': bairro,
            'logradouro': logradouro,
            'numero': numero,
            'status': status,
            'complemento': complemento
        }

        return response

    def listar_pessoas(self):

        # conectando ao banco
        conn = conectar_db()
        connection = conn['connection']

        # criando um cursor
        cursor = connection.cursor(cursor_factory=DictCursor)

        cursor.execute(f"SELECT * FROM pessoas;")

        connection.commit()

        response = cursor.fetchall()

        # fechando conexão com banco.
        fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])

        return response

    def encontrar_pessoa_por_id(self, pessoa_id):

        # conectando ao banco
        conn = conectar_db()
        connection = conn['connection']

        # criando um cursor
        cursor = connection.cursor(cursor_factory=DictCursor)

        try:
            cursor.execute(f"SELECT * FROM pessoas WHERE id = {pessoa_id};")

            connection.commit()

            response = cursor.fetchall()

            # fechando conexão com banco.
            fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])

            return response

        except:
            return 'Ocorreu um erro ao selecionar clientes.'

    def encontrar_pessoa_por_nome(self, pessoa_nome):

        # conectando ao banco
        conn = conectar_db()
        connection = conn['connection']

        # criando um cursor
        cursor = connection.cursor(cursor_factory=DictCursor)

        try:
            cursor.execute(f"SELECT * FROM pessoas WHERE nome = {pessoa_nome};")

            connection.commit()

            response = cursor.fetchall()

            # fechando conexão com banco.
            fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])

            return response

        except:
            return 'Ocorreu um erro ao selecionar clientes.'


    def deletar_pessoa(self, pessoa_id):

        # conectando ao banco
        conn = conectar_db()
        connection = conn['connection']

        # criando um cursor
        cursor = connection.cursor(cursor_factory=DictCursor)

        try:
            cursor.execute(f"DELETE FROM pessoas WHERE id = {pessoa_id}")
            connection.commit()

            # fechando conexão com banco.
            fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])

            return "Pessoa deletado com sucesso"

        except:
            return 'Ocorreu um erro ao deletar'


    def atualizar_pessoa(self, pessoa_id, dados_atualizados):

        # conectando ao banco
        conn = conectar_db()
        connection = conn['connection']

        # criando um cursor
        cursor = connection.cursor(cursor_factory=DictCursor)

        try:
            cursor.execute(
                f"UPDATE pessoas SET "
                f"nome = '{dados_atualizados['nome']}',"
                f"data_nascimento = '{dados_atualizados['data_nascimento']}',"
                f"telefone = '{dados_atualizados['telefone']}',"
                f"email = '{dados_atualizados['email']}',"
                f"sexo = '{dados_atualizados['sexo']}',"
                f"estado = '{dados_atualizados['estado']}',"
                f"cidade = '{dados_atualizados['cidade']}',"
                f"bairro = '{dados_atualizados['bairro']}',"
                f"logradouro = '{dados_atualizados['logradouro']}',"
                f"numero = '{dados_atualizados['numero']}',"
                f"status = '{dados_atualizados['status']}',"
                f"complemento = '{dados_atualizados['complemento']}'"                
                f"WHERE id = {pessoa_id}")
            connection.commit()

            # fechando conexão com banco.
            fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])

            return "Pessoa atualizada com sucesso"

        except:
            return 'Ocorreu um erro ao atualizar'

