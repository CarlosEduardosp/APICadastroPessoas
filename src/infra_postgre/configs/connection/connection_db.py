import psycopg2
from psycopg2 import pool



def conectar_db():

    connection = None

    try:

        # Criando um pool de conexões
        connection_pool = psycopg2.pool.SimpleConnectionPool(1, 10,
                                                             user="teste_postgre_kadu_user",
                                                             password="PmyhHT6Y2cf7z7kaTrYj4Vl2woF8DHia",
                                                             host="dpg-cn829iacn0vc738kfc8g-a.oregon-postgres.render.com",
                                                             port="5432",
                                                             database="apipessoas")

        connection = connection_pool.getconn()

        # retorna uma variável com a conexão
        return {"connection": connection, "connection_pool": connection_pool}

    except psycopg2.Error as e:
        print(f"Erro ao conectar com o banco: {e}")

