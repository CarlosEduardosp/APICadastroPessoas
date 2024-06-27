from src.infra_postgre.repositorio.imagem_repositorio import InserirImagem
from faker import Faker
from PIL import Image
import psycopg2
import io

faker = Faker()


def test_insert():

    inserir_imagem = InserirImagem()

    # salvando o caminho da imagem
    caminho_da_imagem = 'C:/Users/carol/Downloads/caroline.jpg'

    # Abrir a imagem
    imagem = Image.open(caminho_da_imagem)

    # Salvar a imagem em um objeto BytesIO
    dados_binarios_fake = io.BytesIO()
    imagem.save(dados_binarios_fake, format='JPEG')

    # Converter os dados binários para o tipo bytea
    dados_bytea = psycopg2.Binary(dados_binarios_fake.getvalue())

    inserir_imagem.criar_imagem(
        id_pessoa=12,
        nome=faker.name(),
        imagem=dados_binarios_fake.getvalue()
    )
    print('inserido')


def test_select():

    inserir_imagem = InserirImagem()

    response = inserir_imagem.listar_imagens()

    print(response)


def test_select_id():

    inserir_imagem = InserirImagem()

    response = inserir_imagem.encontrar_imagem_por_id(id_pessoa=1)

    print(response)


def test_delete():

    inserir_imagem = InserirImagem()

    response = inserir_imagem.deletar_imagem(
        id_pessoa=5

    )

    print(response)