from fastapi import APIRouter
from src.main.adapter.adapter_pessoa import AdapterPessoa
from src.main.composer.pessoa_composer import register_pessoa_composer

router = APIRouter()


@router.get('/aniversariantes/{mes}')
def aniversariantes(mes: int):
    """
    :return: Seleciona todas as pessoas que fazem aniversario no mes especificado no banco de dados.
    """

    buscar = AdapterPessoa(
        api_route=register_pessoa_composer(),
        data={}
    )

    response = buscar.select_adapter()

    # lista para adicionar os aniversariantes do mes
    lista_de_aniversariantes = []

    for i in response.body:

        # colocando a data de nascimento completa na variavel
        mes_do_aniversario = i['data_nascimento']

        # fatiando a string para retirar apenas o mes da variavel
        mes_do_aniversario = (mes_do_aniversario[2:4])

        # sanvando o mes como inteiro.
        mes_do_aniversario = int(mes_do_aniversario)

        # se mes de aniversario for igual ao mes enviado, adiciona na lista de aniversariantes.
        if mes == mes_do_aniversario:
            lista_de_aniversariantes.append(i)

    if lista_de_aniversariantes:
        return {"status_code": 200, "body": lista_de_aniversariantes}
    else:
        return {"status_code": 400, "body": "Nenhum Aniversariante para este mês."}
