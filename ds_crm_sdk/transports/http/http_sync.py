"""
Deep Sentinel's HTTP Transport Module
"""
from typing import Optional, Callable, Dict, Tuple
from http import HTTPStatus
import requests
from pydantic import BaseModel
from .base import HTTPMethod, HTTPTransport, HTTPHeaderTokenProvider


class DSHTTPTransport(HTTPHeaderTokenProvider, HTTPTransport):
    """
    DSHTTPTransport is a synchronous HTTP transport class for Deep Sentinel's CRM SDK.
    """

    def __init__(self, token_provider: Callable[[], str]):
        super().__init__(token_provider)

    def send(self, method: HTTPMethod, endpoint: str,
             payload: dict = None, params: dict = None,
             headers: Optional[Dict[str, str]] = None,
             timeout: float = 30.0) -> Tuple[Optional[dict], int]:
        """
        Sends the http request based on the given arguments
        :param method: HTTPMethod Enum
        :param endpoint: CRM service endpoint
        :param payload: payload of the request
        :param params: params, if the request needs params
        :param headers: headers used for the request
        :param timeout: Timeout for the request in seconds
        :return: Tuple with data and status code
        """
        try:
            response = requests.request(
                method=method,
                url=endpoint,
                json=payload if payload else None,
                params=params,
                headers=self.set_headers(headers),
                timeout=timeout
            )
            return response.json(), response.status_code
        except requests.HTTPError as e:
            status = e.response.status_code if e.response else HTTPStatus.INTERNAL_SERVER_ERROR
            return {'error': str(e)}, status
        except Exception as e:
            return {'error': str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR


