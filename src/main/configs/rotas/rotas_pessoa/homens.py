from fastapi import APIRouter
from src.main.adapter.adapter_pessoa import AdapterPessoa
from src.main.composer.pessoa_composer import register_pessoa_composer

router = APIRouter()


@router.get('/homens')
def homens():
    """
    :return: Seleciona todas os homens no banco de dados.
    """

    buscar = AdapterPessoa(
        api_route=register_pessoa_composer(),
        data={}
    )

    response = buscar.select_adapter()

    # lista para adicionar os aniversariantes do mes
    lista_de_pessoas = []

    for i in response.body:

        if i["sexo"] == 'm' or i['sexo'] == 'M':

            lista_de_pessoas.append(i)

    if lista_de_pessoas:
        return {"status_code": 200, "body": lista_de_pessoas}
    else:
        return {"status_code": 400, "body": "Vazio."}
