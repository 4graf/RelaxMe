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
async def add_eeg(eeg: EEGAdd,
                  eeg_service: Annotated[AbstractEEGService, Depends(get_eeg_service)]) \
        -> None:
    """
    Создаёт новую запись с данными ЭЭГ пользователя

        :param eeg: Данные ЭЭГ.
        :param eeg_service: Сервис для работы с ЭЭГ.
    """
    await eeg_service.add_user(eeg)


# @router.get("/{id_}", status_code=status.HTTP_200_OK)
# async def get_user(id_: UUID,
#                    user_service: Annotated[AbstractUserService, Depends(get_user_service)]) \
#         -> User:
#     """
#     Получает данные пользователя по его идентификатору
#
#         :param id_: Идентификатор пользователя.
#         :param user_service: Сервис для работы с пользователями.
#         :return: Данные пользователя.
#     """
#     return await user_service.get_user(id_)

