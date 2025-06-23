from enum import Enum
from typing import Optional, Dict
from pydantic import BaseModel
from abc import ABC, abstractmethod


class HTTPMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"


class HTTPTransport(ABC):
    @abstractmethod
    def send(self, method: HTTPMethod, endpoint: str,
             payload: Optional[BaseModel] = None, params: dict = None,
             headers: Optional[Dict[str, str]] = None) -> dict:
        """
        Abstract method that can be used by sync http concreate classes to send requests
        :param method: HTTPMethod Enum
        :param endpoint: CRM service endpoint
        :param payload: payload of the request: Expects pydantic models
        :param params: params, if the request needs params
        :param headers: headers used for the request
        :return: JSON
        """
        pass


class AsyncHTTPTransport(ABC):
    @abstractmethod
    async def send(self, method: HTTPMethod, endpoint: str,
                   payload: Optional[BaseModel] = None, params: dict = None,
                   headers: Optional[Dict[str, str]] = None) -> dict:
        """
        Abstract method that can be used by async http concreate classes to send requests
        :param method: HTTPMethod Enum
        :param endpoint: CRM service endpoint
        :param payload: payload of the request: Expects pydantic models
        :param params: params, if the request needs params
        :param headers: headers used for the request
        :return: JSON
        """
        pass
