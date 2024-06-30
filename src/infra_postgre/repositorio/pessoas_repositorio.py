from src.infra_postgre.configs.connection.connection_db import conectar_db
from src.infra_postgre.configs.connection.fechar_conexao import fechar_conexao_db
from src.infra_postgre.repositorio.interfaces_repositorio.interface_repositorio import InterfacePessoaRepository
from psycopg2.extras import DictCursor
from typing import Type


class InserirPessoa(InterfacePessoaRepository):

    # método construtor para conexão com banco de dados.
    def __init__(self, conectar_db: Type[conectar_db()]):
        self.conectar_db = conectar_db

    def criar_pessoa(self, nome, data_nascimento, telefone,
                     email, sexo, estado, cidade, bairro,
                     logradouro, numero, status, complemento):
        conn = self.conectar_db()
        connection = conn['connection']
        cursor = connection.cursor(cursor_factory=DictCursor)

        try:
            cursor.execute(
                "INSERT INTO pessoas (nome, data_nascimento, telefone, email, sexo, "
                "estado, cidade, bairro, logradouro, numero, status, complemento) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (nome, data_nascimento, telefone,
                 email, sexo, estado, cidade, bairro,
                 logradouro, numero, status, complemento)
            )
            connection.commit()
            id_pessoa = cursor.lastrowid

            fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])

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

        except Exception as e:
            connection.rollback()
            fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])
            raise e

    def listar_pessoas(self):
        conn = self.conectar_db()
        connection = conn['connection']
        cursor = connection.cursor(cursor_factory=DictCursor)

        try:
            cursor.execute("SELECT * FROM pessoas;")
            response = cursor.fetchall()

            fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])

            return response

        except Exception as e:
            fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])
            raise e

    def encontrar_pessoa_por_id(self, pessoa_id):
        conn = self.conectar_db()
        connection = conn['connection']
        cursor = connection.cursor(cursor_factory=DictCursor)

        try:
            cursor.execute("SELECT * FROM pessoas WHERE id = %s;", (pessoa_id,))
            response = cursor.fetchall()

            fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])

            return response

        except Exception as e:
            fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])
            raise e

    def encontrar_pessoa_por_nome(self, pessoa_nome):
        conn = self.conectar_db()
        connection = conn['connection']
        cursor = connection.cursor(cursor_factory=DictCursor)

        try:
            cursor.execute("SELECT * FROM pessoas WHERE nome = %s;", (pessoa_nome,))
            response = cursor.fetchall()

            fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])

            return response

        except Exception as e:
            fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])
            raise e

    def deletar_pessoa(self, pessoa_id):
        conn = self.conectar_db()
        connection = conn['connection']
        cursor = connection.cursor(cursor_factory=DictCursor)

        try:
            cursor.execute("DELETE FROM pessoas WHERE id = %s;", (pessoa_id,))
            connection.commit()

            fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])

            return "Pessoa deletada com sucesso"

        except Exception as e:
            connection.rollback()
            fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])
            raise e

    def atualizar_pessoa(self, pessoa_id, dados_atualizados):
        conn = self.conectar_db()
        connection = conn['connection']
        cursor = connection.cursor(cursor_factory=DictCursor)

        try:
            cursor.execute(
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
                    dados_atualizados['nome'],
                    dados_atualizados['data_nascimento'],
                    dados_atualizados['telefone'],
                    dados_atualizados['email'],
                    dados_atualizados['sexo'],
                    dados_atualizados['estado'],
                    dados_atualizados['cidade'],
                    dados_atualizados['bairro'],
                    dados_atualizados['logradouro'],
                    dados_atualizados['numero'],
                    dados_atualizados['status'],
                    dados_atualizados['complemento'],
                    pessoa_id
                )
            )
            connection.commit()

            fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])

            return "Pessoa atualizada com sucesso"

        except Exception as e:
            connection.rollback()
            fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])
            raise e
