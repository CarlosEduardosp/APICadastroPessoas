from typing import Type, Dict
from src.main.adapter.adapter_interface.adapter_imagem_interface import RouteInterface as Route
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from src.presenters.errors.http_errors import HttpErrors


class AdapterImagem:

    def __init__(self, api_route: Type[Route], data: Type[Dict]) -> any:
        self.api_route = api_route
        self.data = data
        self.query_data = data.keys()

    def insert_adapter(self):
        if "nome" and "id_pessoa" and "imagem" in self.query_data:
            http_request = HttpRequest(query=self.data)
            response = self.api_route.route_insert_imagem(http_request=http_request)

            return response

        return self.__error()

    def select_adapter(self):
        http_request = HttpRequest(query=self.data)
        response = self.api_route.route_select(http_request=http_request)

        return response

    def select_by_id_adapter(self):
        if "id_pessoa" in self.query_data:
            http_request = HttpRequest(query=self.data)
            response = self.api_route.route_select_by_id(http_request)
            return response

        return self.__error()

    def delete_adapter(self):
        if "id_pessoa" in self.query_data:
            http_request = HttpRequest(query=self.data)
            response = self.api_route.route_delete(http_request)

            return response

        return self.__error()

    def __error(self):
        http_error = HttpErrors()
        return http_error.error_422()