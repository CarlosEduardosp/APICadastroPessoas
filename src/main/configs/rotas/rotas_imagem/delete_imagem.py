import fastapi
from fastapi import APIRouter, HTTPException
from src.main.adapter.adapter_imagem import AdapterImagem
from src.main.composer.imagem_composer import RegisterImagemComposer
from src.infra_postgre.configs.connection.connection_db import conectar_db

router = APIRouter()


@router.delete('/delete_imagem_id/{id}')
async def delete_imagem_id(id: int):

    composer = RegisterImagemComposer(conectar_db)

    # Aqui você pode realizar operações adicionais na imagem, se necessário.
    buscar = AdapterImagem(
        api_route=composer.register_imagem_composer(),
        data={"id_pessoa": id},
    )

    # Obtém a resposta HTTP da imagem
    response = buscar.delete_adapter()

    return response
