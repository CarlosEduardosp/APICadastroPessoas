from pydantic import BaseModel


class ItemUpdate(BaseModel):
    """ classe para update e validar dados de pessoa."""

    id: int
    nome: str
    data_nascimento: str
    telefone: str
    email: str
    sexo: str
    estado: str
    cidade: str
    bairro: str
    logradouro: str
    numero: str
    status: bool
    complemento: str