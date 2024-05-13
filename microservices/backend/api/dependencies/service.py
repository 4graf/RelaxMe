from fastapi import Depends
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from microservices.backend.api.dependencies.session import get_async_db_session
from microservices.backend.repositories.database.eeg_repository import EEGRepository
from microservices.backend.repositories.database.user_repository import UserRepository
from microservices.backend.repositories.rest_api.base import get_async_client
from microservices.backend.repositories.rest_api.stress_repository import StressRepository
from microservices.backend.services.eeg_service import EEGService
from microservices.backend.services.stress_service import StressService
from microservices.backend.services.user_service import UserService


async def get_stress_service(client: AsyncClient = Depends(get_async_client)) -> StressService:
    stress_repo = StressRepository(client=client)
    return StressService(stress_repo=stress_repo)


async def get_user_service(session: AsyncSession = Depends(get_async_db_session)) -> UserService:
    user_repo = UserRepository(session)
    return UserService(user_repo)


async def get_eeg_service(session: AsyncSession = Depends(get_async_db_session)) -> EEGService:
    eeg_repo = EEGRepository(session)
    return EEGService(eeg_repo)
