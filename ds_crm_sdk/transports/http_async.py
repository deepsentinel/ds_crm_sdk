import httpx
from .base import HTTPMethod, AsyncHTTPTransport
from typing import Optional, Callable, Dict
from pydantic import BaseModel


class DSHTTPTransport(AsyncHTTPTransport):
    def __init__(self, token_provider: Callable[[], str]):
        self.token_provider = token_provider

    def _headers(self, extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        headers = extra.copy() if extra else dict()
        if self.token_provider and callable(self.token_provider):
            headers["Authorization"] = f"Bearer {self.token_provider()}"
        return headers

    async def send(self, method: HTTPMethod, endpoint: str,
                   payload: Optional[BaseModel] = None, params: dict = None,
                   headers: Optional[Dict[str, str]] = None) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.request(
                method=method,
                url=endpoint,
                json=payload.dict() if payload else None,
                params=params,
                headers=self._headers(headers)
            )
            response.raise_for_status()
            return response.json()

