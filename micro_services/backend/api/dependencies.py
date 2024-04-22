from fastapi import Depends
from httpx import AsyncClient

from micro_services.backend.repositories.base import get_async_client
from micro_services.backend.repositories.rest_api.stress_repository import StressRepository
from micro_services.backend.services.stress_service import StressService


async def get_stress_service(client: AsyncClient = Depends(get_async_client)) -> StressService:
    stress_repo = StressRepository(client=client)
    return StressService(stress_repo=stress_repo)
