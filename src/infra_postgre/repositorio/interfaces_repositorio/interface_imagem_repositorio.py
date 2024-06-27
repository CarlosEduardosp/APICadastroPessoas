from abc import ABC, abstractmethod
from sqlalchemy.orm import Session


class InterfaceImagemRepository(ABC):
    @abstractmethod
    def criar_imagem(self, id_pessoa, nome, imagem):
        pass

    @abstractmethod
    def listar_imagens(self):
        pass

    @abstractmethod
    def encontrar_imagem_por_id(self, id_pessoa):
        pass

    @abstractmethod
    def deletar_imagem(self, id_pessoa):
        pass
