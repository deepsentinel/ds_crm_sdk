from enum import Enum
from typing import Optional, Dict
from pydantic import BaseModel


class HTTPMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"


class HTTPTransport:
    def send(self, method: HTTPMethod, endpoint: str,
             payload: Optional[BaseModel] = None, params: dict = None,
             headers: Optional[Dict[str, str]] = None) -> dict:
        raise NotImplementedError


class AsyncHTTPTransport:
    async def send(self, method: HTTPMethod, endpoint: str,
                   payload: Optional[BaseModel] = None, params: dict = None,
                   headers: Optional[Dict[str, str]] = None) -> dict:
        raise NotImplementedError
