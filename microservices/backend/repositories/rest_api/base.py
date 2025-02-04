from abc import ABC
from typing import Any

from httpx import AsyncClient, Response


class BaseRestApiRepository(ABC):
    base_endpoint: str

    def __init__(self, client: AsyncClient):
        client.base_url = self.base_endpoint
        self.client = client

    async def get(self, url: str) -> Response:
        return await self.client.post(url)

    async def post(self, url: str, payload: Any) -> Response:
        return await self.client.post(url, json=payload)


async def get_async_client():
    async with AsyncClient() as client:  # ToDo: Подумать над необходимостью такой конструкции именно тут
        try:
            yield client
        finally:
            await client.aclose()
