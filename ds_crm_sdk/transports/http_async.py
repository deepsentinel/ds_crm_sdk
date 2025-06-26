import httpx
from .base import HTTPMethod, AsyncHTTPTransport
from typing import Optional, Callable, Dict, Tuple
from pydantic import BaseModel
from http import HTTPStatus


class DSAsyncHTTPTransport(AsyncHTTPTransport):
    def __init__(self, token_provider: Callable[[], str]):
        self.token_provider = token_provider

    def _headers(self, extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        """
        Method that sets the header with the given key, value pairs
        :param extra: Additional header fields, if needed
        :return: Dict of header fields and values
        """
        headers = extra.copy() if extra else dict()
        if self.token_provider and callable(self.token_provider):
            headers["Authorization"] = f"{self.token_provider()}"
        return headers

    async def send(self, method: HTTPMethod, endpoint: str,
                   payload: Optional[BaseModel] = None, params: dict = None,
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
                    json=payload.dict() if payload else None,
                    params=params,
                    headers=self._headers(headers)
                )
                return await response.json(), response.status_code
            except httpx.HTTPStatusError as e:
                status = e.response.status_code if e.response else HTTPStatus.INTERNAL_SERVER_ERROR
                return {'error': str(e)}, status
            except Exception as e:
                return {'error': str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR

