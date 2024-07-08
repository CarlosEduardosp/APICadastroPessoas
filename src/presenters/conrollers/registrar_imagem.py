from typing import Type
from src.use_cases.case_imagem import Registrarimagem
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from src.presenters.conrollers.interface_controller.interface_imagem_controller import RouteInterface
from src.models.imagem_models import Imagem

class RegisterImagemController(RouteInterface):
    """ Class controller """

    def __init__(self, register_imagem_use_case: Type[Registrarimagem]):
        self.register_imagem_use_case = register_imagem_use_case

    def route_insert_imagem(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ method to call use case """

        response = None

        if http_request.query:

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if(
                "nome" in query_string_params and
                "id_pessoa" in query_string_params and
                "imagem" in query_string_params
            ):
                nome = http_request.query['nome']
                id_pessoa = http_request.query['id_pessoa']
                imagem = http_request.query['imagem']

                dados_imagem = Imagem(
                    nome=nome,
                    id_pessoa=id_pessoa,
                    imagem=imagem,
                    id_imagem=0
                )

                response = self.register_imagem_use_case.inseririmagem(
                    dados_imagem
                )

            else:
                response = {'success': False, 'data': None}

            if response["success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["data"])

            # If no query in http_request
            http_error = HttpErrors.error_400()
            return HttpResponse(
                status_code=http_error["status_code"], body=http_error["body"]
            )

    def route_select(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ select all controllers"""

        try:

            response = self.register_imagem_use_case.select_imagem()


            return HttpResponse(status_code=200, body=response['data'])

        except:
            return {'success': False, "data": None}

    def route_select_by_id(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ select by id controller """

        if http_request.query:

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if "id_pessoa" in query_string_params:

                response = self.register_imagem_use_case.select_by_id_imagem(http_request.query['id_pessoa'])
                if response['success']:
                    return HttpResponse(status_code=200, body=response['data'])
                else:
                    return HttpResponse(status_code=400, body=response['data'])
            else:
                response = {'success': False, 'data': None}

        if response["success"] is False:
            http_error = HttpErrors.error_422()
            return HttpResponse(
                status_code=http_error["status_code"], body=http_error["body"]
            )

        return HttpResponse(status_code=200, body=response["data"])

        # If no query in http_request
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    def route_delete(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ delete controller """

        if http_request.query:

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if "id_pessoa" in query_string_params:

                pessoa_id = http_request.query['id_pessoa']

                response = self.register_imagem_use_case.delete_imagem(id_pessoa=pessoa_id)

                return HttpResponse(status_code=200, body=response['data'])
            else:
                response = {'success': False, 'data': None}

        if response["success"] is False:
            http_error = HttpErrors.error_422()
            return HttpResponse(
                status_code=http_error["status_code"], body=http_error["body"]
            )

        return HttpResponse(status_code=200, body=response["data"])

        # If no query in http_request
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
