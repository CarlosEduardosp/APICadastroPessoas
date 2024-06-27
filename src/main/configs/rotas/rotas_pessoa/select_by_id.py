from fastapi import APIRouter
from src.main.adapter.adapter_pessoa import AdapterPessoa
from src.main.composer.pessoa_composer import register_pessoa_composer
from src.main.validacao.validar_entrada.validar_dados_entrada import Validar_dados_entrada

router = APIRouter()


@router.get('/selectid/{id}')
def select_by_id(id: int):

    resposta = Validar_dados_entrada(id=id)

    if resposta:

        buscar = AdapterPessoa(
            api_route=register_pessoa_composer(),
            data={
                "pessoa_id": id
            }
        )

        response = buscar.select_by_id_adapter()

        return response

    else:
        return resposta
