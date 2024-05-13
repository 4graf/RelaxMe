"""
API-маршруты для управления пользователями.
"""
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from starlette import status

from microservices.backend.api.dependencies.service import get_user_service
from microservices.backend.interfaces.services.abstract_user_service import AbstractUserService
from microservices.backend.schemas.user import UserAdd, User

router = APIRouter()


@router.post("/add", status_code=status.HTTP_201_CREATED)
async def add_user(user: UserAdd,
                   user_service: Annotated[AbstractUserService, Depends(get_user_service)]) \
        -> None:
    """
    Создаёт нового пользователя

        :param user: Данные нового пользователя.
        :param user_service: Сервис для работы с пользователями.
    """
    await user_service.add_user(user)


@router.get("/all", status_code=status.HTTP_200_OK)
async def get_users(user_service: Annotated[AbstractUserService, Depends(get_user_service)]) \
        -> list[User]:
    """
    Получает данные всех пользователей

        :param user_service: Сервис для работы с пользователями.
        :return: Данные пользователя.
    """
    return await user_service.get_all_users()


@router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_user(user_id: UUID,
                   user_service: Annotated[AbstractUserService, Depends(get_user_service)]) \
        -> User:
    """
    Получает данные пользователя по его идентификатору

        :param user_id: Идентификатор пользователя.
        :param user_service: Сервис для работы с пользователями.
        :return: Данные пользователя.
    """
    return await user_service.get_user(user_id)
