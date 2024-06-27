from typing import Type, Dict
from src.main.adapter.adapter_interface.adapter_pessoa_interface import RouteInterface as Route
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from src.presenters.errors.http_errors import HttpErrors


class AdapterPessoa:

    def __init__(self, api_route: Type[Route], data: Type[Dict]) -> any:
        self.api_route = api_route
        self.data = data
        self.query_data = data.keys()

    def insert_adapter(self):
        if "nome" and "data_nascimento" and "telefone" and "email" and "sexo" and "estado" and "cidade" \
                and "bairro" and "logradouro" and "numero" and "status" and "complemento" in self.query_data:
            http_request = HttpRequest(query=self.data)
            response = self.api_route.route_insert(http_request)

            return response

        return self.__error()

    def select_adapter(self):
        http_request = HttpRequest(query=self.data)
        response = self.api_route.route_select(http_request=http_request)

        return response

    def select_by_id_adapter(self):
        if "pessoa_id" in self.query_data:
            http_request = HttpRequest(query=self.data)
            response = self.api_route.route_select_by_id(http_request)
            return response

        return self.__error()

    def select_by_name_adapter(self):
        if "nome" in self.query_data:
            http_request = HttpRequest(query=self.data)
            response = self.api_route.route_select_by_name(http_request)
            return response

        return self.__error()

    def delete_adapter(self):
        if "pessoa_id" in self.query_data:
            http_request = HttpRequest(query=self.data)
            response = self.api_route.route_delete(http_request)

            return response

        return self.__error()

    def update_adapter(self):
        if (
            "pessoa_id"
            and "nome"
            and "data_nascimento"
            and "telefone"
            and "email"
            and "telefone"
            and "sexo"
            and "estado"
            and "cidade"
            and "bairro"
            and "logradouro"
            and "numero"
            and "status"
            and "complemento"
            in self.query_data
        ):
            http_request = HttpRequest(query=self.data)
            response = self.api_route.route_update(http_request)

            return response

        return self.__error()

    def __error(self):
        http_error = HttpErrors()
        return http_error.error_422()