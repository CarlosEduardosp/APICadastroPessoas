from fastapi import APIRouter
from src.main.adapter.adapter_pessoa import AdapterPessoa
from src.main.composer.pessoa_composer import RegisterPessoaComposer
from src.infra_postgre.configs.connection.connection_db import conectar_db

router = APIRouter()


@router.get('/mulheres')
def mulheres():
    """
    :return: Seleciona todas os homens no banco de dados.
    """

    composer = RegisterPessoaComposer(conectar_db)

    buscar = AdapterPessoa(
        api_route=composer.register_pessoa_composer(),
        data={}
    )

    response = buscar.select_adapter()

    # lista para adicionar os aniversariantes do mes
    lista_de_pessoas = []

    for i in response.body:

        if i["sexo"] == 'f' or i['sexo'] == 'F':

            lista_de_pessoas.append(i)

    if lista_de_pessoas:
        return {"status_code": 200, "body": lista_de_pessoas}
    else:
        return {"status_code": 400, "body": "Vazio."}
