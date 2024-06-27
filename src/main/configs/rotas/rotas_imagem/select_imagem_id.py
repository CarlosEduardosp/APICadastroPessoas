import fastapi
from fastapi.responses import StreamingResponse
from fastapi import APIRouter, HTTPException
from src.main.adapter.adapter_imagem import AdapterImagem
from src.main.composer.imagem_composer import register_imagem_composer
import io

router = APIRouter()


@router.get('/select_imagem_id')
async def select_imagem_id(id_pessoa: int):

    # Aqui você pode realizar operações adicionais na imagem, se necessário.
    buscar = AdapterImagem(
        api_route=register_imagem_composer(),
        data={"id_pessoa": id_pessoa},
    )

    # Obtém a resposta HTTP da imagem
    imagem = buscar.select_by_id_adapter()
    
    if imagem.status_code == 200:

        imagem = imagem.body[0]['imagem']

        print(type(imagem))
        if isinstance(imagem, memoryview):

            imagem = StreamingResponse(io.BytesIO(imagem), media_type="image/jpeg")
            return imagem
    else:
        return imagem
