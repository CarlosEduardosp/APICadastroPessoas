from abc import ABC, abstractmethod
from sqlalchemy.orm import Session


class InterfacePessoaUsecse(ABC):
    @abstractmethod
    def inserirpessoa(
            self,
            nome: str,
            data_nascimento: str,
            telefone: str,
            email: str,
            sexo: str,
            estado: str,
            cidade: str,
            bairro: str,
            logradouro: str,
            numero: str,
            status: bool,
            complemento: str
    ):
        pass

    @abstractmethod
    def select_pessoas(self):
        pass

    @abstractmethod
    def select_by_id(self, pessoa_id: int):
        pass

    @abstractmethod
    def select_by_nome(self, nome: str):
        pass

    @abstractmethod
    def atualizar_dados(self,pessoa_id: int, dados_atualizados: dict):
        pass

    @abstractmethod
    def delete(self, pessoa_id: int):
        pass
