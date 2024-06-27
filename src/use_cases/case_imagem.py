from src.infra_postgre.repositorio.imagem_repositorio import InserirImagem
from src.use_cases.interface_use_case.interface_use_case_imagem import InterfaceImagemUsecase
from typing import Type


class Registrarimagem(InterfaceImagemUsecase):
    """ Caso de uso para registrar uma pessoa """

    def __init__(self, imagem_repository: Type[InserirImagem]):
        self.imagem_repository = imagem_repository

    def inseririmagem(
            self,
            id_pessoa: int,
            nome: str,
            imagem: bytes
    ):
        """ Inserir pessoa """

        validade_entry = isinstance(id_pessoa, int)

        if validade_entry:
            response = self.imagem_repository.criar_imagem(
                id_pessoa=id_pessoa,
                nome=nome,
                imagem=imagem
            )

            return {'success': True, 'data': response}
        else:
            return {'success': False, 'data': None}

    def select_imagem(self):
        """ selecionar pessoas """

        response = self.imagem_repository.listar_imagens()

        return {'success': True, 'data': response}

    def select_by_id_imagem(self, id_pessoa: int):
        """ selecting by id"""

        validate_entry = isinstance(id_pessoa, int)

        if validate_entry:
            response = self.imagem_repository.encontrar_imagem_por_id(id_pessoa=id_pessoa)
            if response:
                return {'success': True, 'data': response}
            else:
                return {'success': False, 'data': 'Nada encontrado com o valor passado.'}
        else:
            raise ValueError('pessoa_id deve ser inteiro.')

    def delete_imagem(self, id_pessoa: int):
        """ use case delete """

        validade_entry = isinstance(id_pessoa, int)

        if validade_entry:
            response = self.imagem_repository.deletar_imagem(id_pessoa=id_pessoa)
            return {'success': True, 'data': response}
        else:
            raise ValueError('Pessoa_id deve ser inteiro.')

