from .calculo_idade import calcular_idade


def test_calcularIdade():

    response = calcular_idade('11111994')

    print(response)
