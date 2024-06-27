from src.infra_postgre.repositorio.pessoas_repositorio import InserirPessoa
from src.use_cases.interface_use_case.interface_use_case import InterfacePessoaUsecse
from typing import Type


class Registrarpessoa(InterfacePessoaUsecse):
    """ Caso de uso para registrar uma pessoa """

    def __init__(self, pessoa_repository: Type[InserirPessoa]):
        self.pessoa_repository = pessoa_repository

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
        """ Inserir pessoa """

        validade_entry = self.__validar_dados(
            nome,
            data_nascimento,
            telefone,
            email,
            sexo,
            estado,
            cidade,
            bairro,
            logradouro,
            numero,
            status,
            complemento
        )

        if validade_entry:
            response = self.pessoa_repository.criar_pessoa(
                nome=nome,
                data_nascimento=data_nascimento,
                telefone=telefone,
                email=email,
                sexo=sexo,
                estado=estado,
                cidade=cidade,
                bairro=bairro,
                logradouro=logradouro,
                numero=numero,
                status=status,
                complemento=complemento
            )
            return {'success': True, 'data': response}
        else:
            return {'success': False, 'data': None}

    def select_pessoas(self):
        """ selecionar pessoas """

        response = self.pessoa_repository.listar_pessoas()

        return {'success': True, 'data': response}

    def select_by_id(self, pessoa_id: int):
        """ selecting by id"""

        validate_entry = isinstance(pessoa_id, int)

        if validate_entry:
            response = self.pessoa_repository.encontrar_pessoa_por_id(pessoa_id=pessoa_id)
            if response:
                return {'success': True, 'data': response}
            else:
                return {'success': False, 'data': 'Nada encontrado com o valor passado.'}
        else:
            raise ValueError('pessoa_id deve ser inteiro.')
        
    def select_by_nome(self, nome: str):
        """ selecting by nome"""

        validate_entry = isinstance(nome, str)

        if validate_entry:
            response = self.pessoa_repository.encontrar_pessoa_por_nome(nome)
            if response:
                return {'success': True, 'data': response}
            else:
                return {'success': False, 'data': 'Nada encontrado com o Nome passado, passe o nome completo conforme '
                                                  'cadastro.'}
        else:
            raise ValueError('nome deve ser uma string.')

    def atualizar_dados(self,pessoa_id: int, dados_atualizados: dict):
        """ Atualizando dados de pessoas """

        validade_entry = self.__validar_dados(
                nome=dados_atualizados['nome'],
                data_nascimento=dados_atualizados['data_nascimento'],
                telefone=dados_atualizados['telefone'],
                email=dados_atualizados['email'],
                sexo=dados_atualizados['sexo'],
                estado=dados_atualizados['estado'],
                cidade=dados_atualizados['cidade'],
                bairro=dados_atualizados['bairro'],
                logradouro=dados_atualizados['logradouro'],
                numero=dados_atualizados['numero'],
                status=dados_atualizados['status'],
                complemento=dados_atualizados['complemento'])

        if validade_entry:
            response = self.pessoa_repository.atualizar_pessoa(pessoa_id=pessoa_id, dados_atualizados=dados_atualizados)
            return {'success': True, 'data': response}

        return {'success': False, 'data': self.__error()}

    def delete(self, pessoa_id: int):
        """ use case delete """

        validade_entry = isinstance(pessoa_id, int)

        if validade_entry:
            response = self.pessoa_repository.deletar_pessoa(pessoa_id=pessoa_id)
            return {'success': True, 'data': response}
        else:
            raise ValueError('Pessoa_id deve ser inteiro.')

    def __validar_dados(
        self,
        nome: str = "",
        data_nascimento: str = "",
        telefone: str = "",
        email: str = "@",
        sexo: str = "",
        estado: str = "",
        cidade: str = "",
        bairro: str = "",
        logradouro: str = "",
        numero: str = "",
        status: bool = True,
        complemento: str = ''
    ) -> bool:
        """ Validador de dados """

        if not isinstance(nome, str):
            raise ValueError("Nome deve ser uma String")

        if not isinstance(data_nascimento, str):
            raise ValueError("data_nascimento deve ser uma string")

        if not isinstance(email, str):
            return {"success": False, "data": "Email precisa ser uma string."}

        if "@" not in email:
            raise ValueError("@ precisa estar no email.")

        if not isinstance(telefone, str):
            raise ValueError("telefone deve ser uma string")

        if not isinstance(sexo, str):
            raise ValueError("Sexo deve ser uma string.")

        if not isinstance(estado, str):
            raise ValueError("estado deve ser uma string")

        if not isinstance(cidade, str):
            raise ValueError("cidade deve ser uma string")

        if not isinstance(bairro, str):
            raise ValueError("bairro deve ser uma string")

        if not isinstance(logradouro, str):
            raise ValueError("logradouro deve ser uma string")

        if not isinstance(numero, str):
            raise ValueError("numero deve ser uma string")
        
        if not isinstance(complemento, str):
            raise ValueError("complemento deve ser uma string")

        if not isinstance(status, bool):
            raise ValueError("Status deve ser um Boolean")

        return True

    def __error(self, response: str = None):
        """ Mensagem de erro """
        return {"Success": False, "Data": response}



