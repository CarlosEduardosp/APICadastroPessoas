from fastapi import APIRouter
from src.main.adapter.adapter_pessoa import AdapterPessoa
from src.main.composer.pessoa_composer import RegisterPessoaComposer
from src.infra_postgre.configs.connection.connection_db import conectar_db
from src.main.validacao.classModelsvalidar.update_validar import ItemUpdate
from src.main.validacao.validar_entrada.validar_dados_entrada import Validar_dados_entrada
from src.main.validacao.ValidarNoBanco.validar_dados_no_banco import conferir_pessoa_no_banco

router = APIRouter()


@router.put('/update')
def update(item: ItemUpdate):

    resposta = Validar_dados_entrada(
        nome=item.nome,
        data_nascimento=item.data_nascimento,
        telefone=item.telefone,
        email=item.email,
        sexo=item.sexo,
        estado=item.estado,
        cidade=item.cidade,
        bairro=item.bairro,
        logradouro=item.logradouro,
        numero=item.numero,
        status=item.status,
        complemento=item.complemento,
        id=item.id
    )

    if resposta['success']:

        composer = RegisterPessoaComposer(conectar_db)

        buscar = AdapterPessoa(
            api_route=composer.register_pessoa_composer(),
            data={
                "id": item.id,
                "nome": item.nome,
                "data_nascimento": item.data_nascimento,
                "telefone": item.telefone,
                "email": item.email,
                "sexo": item.sexo,
                "estado": item.estado,
                "cidade": item.cidade,
                "bairro": item.bairro,
                "logradouro": item.logradouro,
                "numero": item.numero,
                "status": item.status,
                "complemento": item.complemento
            },
        )
        response = buscar.update_adapter()

        try:
            if response.status_code == 200:
                return {"success": True, "data": "Atualização feita com Sucesso"}
        except:
            return response

    else:
        return resposta
