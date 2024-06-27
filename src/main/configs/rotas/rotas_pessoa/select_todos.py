from fastapi import APIRouter
from src.main.adapter.adapter_pessoa import AdapterPessoa
from src.main.composer.pessoa_composer import register_pessoa_composer
from fastapi.responses import StreamingResponse
import io

router = APIRouter()


@router.get('/select_todos')
def select_todos():
    """
    :return: Seleciona todas as pessoas do banco de dados.
    """

    buscar = AdapterPessoa(
        api_route=register_pessoa_composer(),
        data={}
    )

    response = buscar.select_adapter()

    return response


