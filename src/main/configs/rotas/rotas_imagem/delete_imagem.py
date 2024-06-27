import fastapi
from fastapi import APIRouter, HTTPException
from src.main.adapter.adapter_imagem import AdapterImagem
from src.main.composer.imagem_composer import register_imagem_composer

router = APIRouter()


@router.delete('/delete_imagem_id/{id}')
async def delete_imagem_id(id: int):

    # Aqui você pode realizar operações adicionais na imagem, se necessário.
    buscar = AdapterImagem(
        api_route=register_imagem_composer(),
        data={"id_pessoa": id},
    )

    # Obtém a resposta HTTP da imagem
    response = buscar.delete_adapter()

    return response
