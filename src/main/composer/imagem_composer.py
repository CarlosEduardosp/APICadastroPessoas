from src.main.adapter.adapter_interface.adapter_imagem_interface import RouteInterface
from src.presenters.conrollers.registrar_imagem import RegisterImagemController
from src.use_cases.case_imagem import Registrarimagem
from src.infra_postgre.repositorio.imagem_repositorio import InserirImagem
from src.infra_postgre.configs.connection.connection_db import conectar_db
from typing import Type


class RegisterImagemComposer:
    def __init__(self, conectar_db: Type[conectar_db] ):
        self.conectar_db = conectar_db

    def register_imagem_composer(self) -> RouteInterface:
        """ composing register pessoa route """

        repository = InserirImagem(self.conectar_db)
        use_case = Registrarimagem(repository)
        registrar_imagem_route = RegisterImagemController(use_case)

        return registrar_imagem_route
