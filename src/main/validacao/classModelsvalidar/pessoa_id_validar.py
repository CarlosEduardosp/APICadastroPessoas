from pydantic import BaseModel


class PessoaId(BaseModel):
    """ validação do id """

    pessoa_id: int
