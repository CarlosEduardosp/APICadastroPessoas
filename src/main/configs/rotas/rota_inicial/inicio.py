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
        "Message": "Api backend Cadastro de Pessoas, Banco PostgreSQL, rodando perfeitamente.",
        "Versão": 1.0,
        "Info": "Use '(link)/docs' para acessar a documentação no Swagger ",
        "Dev": "Carlos Eduardo dos S. Padilha"
    }

    return response

