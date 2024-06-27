from src.main.adapter.adapter_interface.adapter_imagem_interface import RouteInterface
from src.presenters.conrollers.registrar_imagem import RegisterImagemController
from src.use_cases.case_imagem import Registrarimagem
from src.infra_postgre.repositorio.imagem_repositorio import InserirImagem


def register_imagem_composer() -> RouteInterface:
    """ composing register pessoa route """

    repository = InserirImagem()
    use_case = Registrarimagem(repository)
    registrar_imagem_route = RegisterImagemController(use_case)

    return registrar_imagem_route
