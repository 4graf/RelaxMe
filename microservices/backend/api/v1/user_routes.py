"""
API-маршруты для управления пользователями.
"""
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from starlette import status
from starlette.exceptions import HTTPException

from microservices.backend.api.dependencies.service import get_user_service
from microservices.backend.exceptions.user_esceptions import UserNotFoundException
from microservices.backend.interfaces.services.abstract_user_service import AbstractUserService
from microservices.backend.schemas.user import UserLogin, User

router = APIRouter()


@router.post("/login", status_code=status.HTTP_200_OK)
async def login_user(user: UserLogin,
                     user_service: Annotated[AbstractUserService, Depends(get_user_service)]) \
        -> User:
    """
    Создаёт нового пользователя

        :param user: Данные нового пользователя.
        :param user_service: Сервис для работы с пользователями.
    """
    return await user_service.login_user(user)


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
    try:
        return await user_service.get_user(user_id)
    except UserNotFoundException as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=str(exc)) from exc
