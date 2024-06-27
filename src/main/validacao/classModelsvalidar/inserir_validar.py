from pydantic import BaseModel


class Item(BaseModel):
    """ classe para inserir e validar dados de pessoa."""

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
