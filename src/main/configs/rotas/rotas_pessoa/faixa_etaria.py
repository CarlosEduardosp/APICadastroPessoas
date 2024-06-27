from fastapi import APIRouter
from src.main.adapter.adapter_pessoa import AdapterPessoa
from src.main.composer.pessoa_composer import register_pessoa_composer

router = APIRouter()


@router.get('/faixaetaria/{valor1}/{valor2}')
def faixa_etaria(valor1: int, valor2: int):
    """
    :return: Seleciona pessoas entre uma faixa de idade.
    """

    buscar = AdapterPessoa(
        api_route=register_pessoa_composer(),
        data={}
    )

    response = buscar.select_adapter()

    # lista para adicionar os aniversariantes do mes
    lista_de_pessoas = []

    for i in response.body:

        if i["idade"] >= valor1 and i['idade'] <= valor2:

            lista_de_pessoas.append(i)

    if lista_de_pessoas:
        return {"status_code": 200, "body": lista_de_pessoas}
    else:
        if valor1 > valor2:
            return {"status_code": 410, "body": "O Primeiro valor precisa ser maior que o segundo valor passado."}
        else:
            return {"status_code": 400, "body": "Lista Vazia."}
