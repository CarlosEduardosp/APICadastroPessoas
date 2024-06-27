from abc import ABC, abstractmethod
from sqlalchemy.orm import Session


class InterfaceImagemUsecase(ABC):
    @abstractmethod
    def inseririmagem(
            self,
            id_pessoa: int,
            nome: str,
            imagem: bytes
    ):
        pass

    @abstractmethod
    def select_imagem(self):
        pass

    @abstractmethod
    def select_by_id_imagem(self, id_pessoa: int):
        pass
   
    @abstractmethod
    def delete_imagem(self, id_pessoa: int):
        pass
