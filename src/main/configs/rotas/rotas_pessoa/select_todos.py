from fastapi import APIRouter
from src.main.adapter.adapter_pessoa import AdapterPessoa
from src.main.composer.pessoa_composer import RegisterPessoaComposer
from src.infra_postgre.configs.connection.connection_db import conectar_db
from fastapi.responses import StreamingResponse
import io

router = APIRouter()


@router.get('/select_todos')
def select_todos():
    """
    :return: Seleciona todas as pessoas do banco de dados.
    """

    composer = RegisterPessoaComposer(conectar_db)

    buscar = AdapterPessoa(
        api_route=composer.register_pessoa_composer(),
        data={}
    )

    response = buscar.select_adapter()

    return response


