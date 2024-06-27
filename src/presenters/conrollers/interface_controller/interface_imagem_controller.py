from typing import Type
from abc import ABC, abstractmethod
from src.presenters.helpers.http_models import HttpRequest, HttpResponse


class RouteInterface(ABC):
    """Interface to Routes"""

    @abstractmethod
    def route_insert_imagem(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Defining Route"""

        raise Exception("Should implement method: route")

    def route_select_all_imagem(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Defining Route"""

        raise Exception("Should implement method: route")

    def route_select_by_id_imagem(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Defining Route"""

        raise Exception("Should implement method: route")

    def route_delete_imagem(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Defining Route"""

        raise Exception("Should implement method: route")

