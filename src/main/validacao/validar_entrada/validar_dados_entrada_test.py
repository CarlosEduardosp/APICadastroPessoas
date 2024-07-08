from .validar_dados_entrada import Validar_dados_entrada
from faker import Faker

faker = Faker()


def test_validar():

    response = Validar_dados_entrada(
        nome='12345678910',
        data_nascimento='14051986',
        telefone=faker.name(),
        email=faker.email(),
        sexo='M',
        estado=faker.name(),
        cidade=faker.name(),
        bairro=faker.name(),
        logradouro=faker.name(),
        numero=faker.name(),
        status=True,
        id=125
    )

    print(response)
