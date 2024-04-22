"""
Модуль предоставляет API-маршруты для управления всеми микро-сервисами приложения.
"""
from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from micro_services.backend.api.dependencies import get_stress_service
from micro_services.backend.interfaces.services.abstract_stress_service import AbstractStressService
from micro_services.backend.schemas.eeg_data import EEGData
from micro_services.backend.schemas.stress_prediction import StressPrediction

router = APIRouter()


@router.post("/predict", status_code=status.HTTP_200_OK)
async def predict_stress(data_eeg: EEGData,
                         stress_service: Annotated[AbstractStressService, Depends(get_stress_service)]) \
        -> StressPrediction:
    """
    Предсказывает стресс по данным ЭЭГ

        :param data_eeg: Данные ЭЭГ.
        :param stress_service: Сервис для работы со стрессом по ЭЭГ.
        :return: Список с предсказаниями.
    """
    return await stress_service.predict_stress(data_eeg)
