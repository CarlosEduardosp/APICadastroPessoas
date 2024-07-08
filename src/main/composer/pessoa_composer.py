from src.main.adapter.adapter_interface.adapter_pessoa_interface import RouteInterface
from src.presenters.conrollers.registrar_pessoa import RegisterPessoaController
from src.use_cases.case_inserir_pessoa import Registrarpessoa
from src.infra_postgre.repositorio.pessoas_repositorio import InserirPessoa
from src.infra_postgre.configs.connection.connection_db import conectar_db
from typing import Type


class RegisterPessoaComposer:
    def __init__(self, conectar_db: Type[conectar_db] ):
        self.conectar_db = conectar_db

    def register_pessoa_composer(self) -> RouteInterface:
        """ composing register pessoa route """

        repository = InserirPessoa(self.conectar_db)
        use_case = Registrarpessoa(repository)
        registrar_pessoa_route = RegisterPessoaController(use_case)

        return registrar_pessoa_route
