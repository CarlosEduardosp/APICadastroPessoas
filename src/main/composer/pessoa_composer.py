from src.main.adapter.adapter_interface.adapter_pessoa_interface import RouteInterface
from src.presenters.conrollers.registrar_pessoa import RegisterPessoaController
from src.use_cases.case_inserir_pessoa import Registrarpessoa
from src.infra_postgre.repositorio.pessoas_repositorio import InserirPessoa


def register_pessoa_composer() -> RouteInterface:
    """ composing register pessoa route """

    repository = InserirPessoa()
    use_case = Registrarpessoa(repository)
    registrar_pessoa_route = RegisterPessoaController(use_case)

    return registrar_pessoa_route
