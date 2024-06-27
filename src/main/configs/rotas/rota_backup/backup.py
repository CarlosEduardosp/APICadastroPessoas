from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from .agenda_backup import minha_funcao

router = APIRouter()

def enviar_backup():
    """
    :return:envia backup por email.
    """

    response = minha_funcao()

    return response
