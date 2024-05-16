"""
API-маршруты для управления пользователями.
"""
from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from microservices.backend.api.dependencies.service import get_eeg_service
from microservices.backend.interfaces.services.abstract_eeg_service import AbstractEEGService
from microservices.backend.schemas.eeg import EEGAdd, EEGInfo

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
    await eeg_service.add_eeg(eeg)


@router.get("/all", status_code=status.HTTP_200_OK)
async def get_all_eeg(eeg_service: Annotated[AbstractEEGService, Depends(get_eeg_service)]) \
        -> list[EEGInfo]:
    """
    Получает все записи ЭЭГ

        :param eeg_service: Сервис для работы с ЭЭГ.
    """
    return await eeg_service.get_all_eeg()
