from fastapi import APIRouter
from fastapi.responses import StreamingResponse

router = APIRouter()


@router.get('/')
def inicio():
    """
    :return: Mensagem de inicio na api.
    """

    response = {
        "Success": 200,
        "Message": "Api backend Icnv-Araruama, Banco Postgre, rodando perfeitamente.",
        "Versão": 2.0,
        "Info": "Use https://icnvback.onrender.com/docs para acessar a documentação no Swagger ",
        "Dev": "Carlos Eduardo dos S. Padilha"
    }

    return response

