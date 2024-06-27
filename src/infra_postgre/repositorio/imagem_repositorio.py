from src.infra_postgre.configs.connection.connection_db import conectar_db
from src.infra_postgre.configs.connection.fechar_conexao import fechar_conexao_db
from src.infra_postgre.repositorio.interfaces_repositorio.interface_imagem_repositorio import InterfaceImagemRepository
from psycopg2.extras import DictCursor

class InserirImagem(InterfaceImagemRepository):

    def criar_imagem(self, id_pessoa, nome, imagem):

        # conectando ao banco
        conn = conectar_db()
        connection = conn['connection']

        # criando um cursor
        cursor = connection.cursor(cursor_factory=DictCursor)

        #Executar a inserção na tabela do PostgreSQL
        cursor.execute(
            "INSERT INTO imagem (id_pessoa, nome, imagem) VALUES (%s, %s, %s)",
        (id_pessoa, nome, imagem)
        )


        connection.commit()

        # fechando conexão com banco.
        fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])

        return 'Imagem Inserida com sucesso'


    def listar_imagens(self):

        # conectando ao banco
        conn = conectar_db()
        connection = conn['connection']

        # criando um cursor
        cursor = connection.cursor(cursor_factory=DictCursor)

        cursor.execute(f"SELECT * FROM imagem;")

        connection.commit()

        response = cursor.fetchall()

        # fechando conexão com banco.
        fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])

        return response

    def encontrar_imagem_por_id(self, id_pessoa):

        # conectando ao banco
        conn = conectar_db()
        connection = conn['connection']

        # criando um cursor
        cursor = connection.cursor(cursor_factory=DictCursor)

        try:
            cursor.execute(f"SELECT * FROM imagem WHERE id_pessoa= {id_pessoa};")

            connection.commit()

            response = cursor.fetchall()

            # fechando conexão com banco.
            fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])

            return response

        except:
            return 'Ocorreu um erro ao selecionar clientes.'


    def deletar_imagem(self, id_pessoa):

        # conectando ao banco
        conn = conectar_db()
        connection = conn['connection']

        # criando um cursor
        cursor = connection.cursor(cursor_factory=DictCursor)

        try:
            cursor.execute(f"DELETE FROM imagem WHERE id = {id_pessoa}")
            connection.commit()

            # fechando conexão com banco.
            fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])

            return "Imagem deletado com sucesso"

        except:
            return 'Ocorreu um erro ao deletar'


