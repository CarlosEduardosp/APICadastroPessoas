from fastapi import APIRouter, Form, HTTPException, File, UploadFile
from src.main.adapter.adapter_imagem import AdapterImagem
from src.main.composer.imagem_composer import register_imagem_composer
from PIL import Image
import io

router = APIRouter()


@router.post('/inserir_imagem')
async def inserir_imagem(nome: str, id_pessoa: int, imagem: UploadFile = File(...)):

    # Validar o tipo de arquivo
    if not imagem.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="O arquivo não é uma imagem")

    # Ler a imagem
    contents = await imagem.read()
    img = Image.open(io.BytesIO(contents))

    # Aqui você pode realizar operações adicionais na imagem, se necessário.
    buscar = AdapterImagem(
        api_route=register_imagem_composer(),
        data={
            "nome": nome,
            "id_pessoa": id_pessoa,
            "imagem": contents
        },
    )
    # inserção no banco de dados.
    buscar.insert_adapter()

    # Exemplo de retorno (pode ser ajustado conforme necessário)

    return {"status_code": 200, "mensagem": "Imagem recebida com sucesso"}
