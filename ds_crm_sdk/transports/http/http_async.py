"""
Async HTTP Transport for DS CRM SDK
"""
from http import HTTPStatus
from typing import Optional, Callable, Dict, Tuple
import httpx
from pydantic import BaseModel
from .base import HTTPMethod, AsyncHTTPTransport, HTTPHeaderTokenProvider


class DSAsyncHTTPTransport(HTTPHeaderTokenProvider, AsyncHTTPTransport):
    """
    Async HTTP Transport for DS CRM SDK.
    """
    def __init__(self, token_provider: Callable[[], str]):
        super().__init__(token_provider)

    async def send(self, method: HTTPMethod, endpoint: str,
                   payload: dict = None, params: dict = None,
                   headers: Optional[Dict[str, str]] = None) -> Tuple[Optional[dict], int]:
        """
        Sends the http request based on the given arguments
        :param method: HTTPMethod Enum
        :param endpoint: CRM service endpoint
        :param payload: payload of the request: Expects pydantic models
        :param params: params, if the request needs params
        :param headers: headers used for the request
        :return: Tuple with data and status code
        """
        async with httpx.AsyncClient() as client:
            try:
                response = await client.request(
                    method=method,
                    url=endpoint,
                    json=payload if payload else None,
                    params=params,
                    headers=self.set_headers(headers)
                )
                return await response.json(), response.status_code
            except httpx.HTTPStatusError as e:
                status = e.response.status_code if e.response else HTTPStatus.INTERNAL_SERVER_ERROR
                return {'error': str(e)}, status
            except Exception as e:
                return {'error': str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR


