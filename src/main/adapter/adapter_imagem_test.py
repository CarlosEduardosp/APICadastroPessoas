from src.main.composer.imagem_composer import register_imagem_composer
from src.main.adapter.adapter_imagem import AdapterImagem
from faker import Faker
from PIL import Image
import io

faker = Faker()


def insert_adapter():
    # salvando o caminho da imagem
    caminho_da_imagem = 'C:/Users/carol/Downloads/logoga.jpg'

    # Abrir a imagem
    imagem = Image.open(caminho_da_imagem)

    # Salvar a imagem em um objeto BytesIO
    dados_binarios_fake = io.BytesIO()
    imagem.save(dados_binarios_fake, format='JPEG')

    buscar = AdapterImagem(
        api_route=register_imagem_composer(),
        data={
            "nome": 'testadapter',
            "id_pessoa": 20,
            "imagem": dados_binarios_fake.getvalue()
        },
    )
    response = buscar.insert_adapter()

    print(response)


def select():

    buscar = AdapterImagem(
        api_route=register_imagem_composer(),
        data={}
    )

    response = buscar.select_adapter()

    print(response)


def select_by_id():

    buscar = AdapterImagem(
        api_route=register_imagem_composer(),
        data={"id_pessoa": 20}
    )

    response = buscar.select_by_id_adapter()
    print(response)


def delete_adapter():
    buscar = AdapterImagem(
        api_route=register_imagem_composer(),
        data={
            'id_pessoa': 20
        }
    )

    response = buscar.delete_adapter()
    print(response)

