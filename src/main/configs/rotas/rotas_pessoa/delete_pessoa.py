from fastapi import APIRouter
from src.main.adapter.adapter_pessoa import AdapterPessoa
from src.main.composer.pessoa_composer import RegisterPessoaComposer
from src.infra_postgre.configs.connection.connection_db import conectar_db
from src.main.validacao.classModelsvalidar.pessoa_id_validar import PessoaId
from src.main.validacao.validar_entrada.validar_dados_entrada import Validar_dados_entrada

router = APIRouter()


@router.delete('/delete/{id}')
def delete_pessoa(id: int):

    resposta = Validar_dados_entrada(id=id)

    if resposta:

        composer = RegisterPessoaComposer(conectar_db)

        buscar = AdapterPessoa(
            api_route=composer.register_pessoa_composer(),
            data={
                "pessoa_id": id
            }
        )

        response = buscar.delete_adapter()

        return response

    else:
        return resposta
