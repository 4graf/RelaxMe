from fastapi import Depends
from httpx import AsyncClient

from microservices.backend.repositories.rest_api.base import get_async_client
from microservices.backend.repositories.rest_api.stress_repository import StressRepository
from microservices.backend.services.stress_service import StressService


async def get_stress_service(client: AsyncClient = Depends(get_async_client)) -> StressService:
    stress_repo = StressRepository(client=client)
    return StressService(stress_repo=stress_repo)
