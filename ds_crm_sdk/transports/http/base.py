"""
Base classes for HTTP transport layer
"""
from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional, Dict, Tuple, Callable
from pydantic import BaseModel


class HTTPMethod(str, Enum):
    """
    Enum representing HTTP methods.
    """
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"


class HTTPTransport(ABC):
    """
    Interface for synchronous HTTP transport.
    """
    @abstractmethod
    def send(self, method: HTTPMethod, endpoint: str,
             payload: Optional[BaseModel] = None, params: dict = None,
             headers: Optional[Dict[str, str]] = None) -> Tuple[Optional[dict], int]:
        """
        Abstract method that can be used by sync http concreate classes to send requests
        :param method: HTTPMethod Enum
        :param endpoint: CRM service endpoint
        :param payload: payload of the request: Expects pydantic models
        :param params: params, if the request needs params
        :param headers: headers used for the request
        :return: Tuple with data and status code
        """


class AsyncHTTPTransport(ABC):
    """
    Interface for asynchronous HTTP transport.
    """
    @abstractmethod
    async def send(self, method: HTTPMethod, endpoint: str,
                   payload: Optional[BaseModel] = None, params: dict = None,
                   headers: Optional[Dict[str, str]] = None) -> Tuple[Optional[dict], int]:
        """
        Abstract method that can be used by async http concreate classes to send requests
        :param method: HTTPMethod Enum
        :param endpoint: CRM service endpoint
        :param payload: payload of the request: Expects pydantic models
        :param params: params, if the request needs params
        :param headers: headers used for the request
        :return: Tuple with data and status code
        """


class HTTPHeaderTokenProvider:
    """
    Base class for HTTP transports that require a token in the headers.
    """
    def __init__(self, token_provider: Optional[Callable[[], str]] = None):
        """
        Initializes the HTTPTokenProvider with an optional token provider function.
        :param token_provider: A callable that returns a string token, e.g., a JWT token.
        """
        self.token_provider = token_provider

    def set_headers(self, extra: dict = None) -> Dict[str, str]:
        """
        Method that sets the header with the given key, value pairs
        :param extra: Additional header fields, if needed
        :return: Dict of header fields and values
        """
        headers = extra.copy() if extra else {}
        if self.token_provider and callable(self.token_provider):
            # Assuming the token provider returns a string token.
            # For jwt token provider can return Bearer <token>
            headers["Authorization"] = f"{self.token_provider()}"
        return headers

