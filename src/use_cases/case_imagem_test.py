import datetime
from src.infra_postgre.repositorio.imagem_repositorio import InserirImagem
from src.use_cases.case_imagem import Registrarimagem
from faker import Faker
from PIL import Image
import psycopg2
import io

faker = Faker()


def test_inserir_use_case():
    """ testes use case """

    # Teste rápidos
    repository = InserirImagem()
    teste = Registrarimagem(repository)

    # salvando o caminho da imagem
    caminho_da_imagem = 'C:/Users/carol/Downloads/caroline.jpg'

    # Abrir a imagem
    imagem = Image.open(caminho_da_imagem)

    # Salvar a imagem em um objeto BytesIO
    dados_binarios_fake = io.BytesIO()
    imagem.save(dados_binarios_fake, format='JPEG')

    # Converter os dados binários para o tipo bytea
    dados_bytea = psycopg2.Binary(dados_binarios_fake.getvalue())

    teste.inseririmagem(
        id_pessoa=12,
        nome=faker.name(),
        imagem=dados_binarios_fake.getvalue()
    )
    print('inserido')


def test_select():
    """ selecting pessoas """

    repository = InserirImagem()
    teste = Registrarimagem(repository)

    response = teste.select_imagem()

    print(response)


def test_select_by_id():
    repository = InserirImagem()
    teste = Registrarimagem(repository)

    response = teste.select_by_id_imagem(id_pessoa=12)

    if response:
        print(response)


def test_delete_use_case():
    repository = InserirImagem()
    teste = Registrarimagem(repository)

    teste.delete_imagem(id_pessoa=12)
