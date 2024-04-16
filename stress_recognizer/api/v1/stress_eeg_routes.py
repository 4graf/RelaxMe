"""
Модуль предоставляет API-маршруты для управления поставщиками.
"""

from fastapi import APIRouter
from starlette import status

from stress_recognizer.services.recognizer_service import RecognizerService

router = APIRouter()


@router.post("/predict", status_code=status.HTTP_200_OK)
async def predict_stress(data_eeg, data_mode, recognizer_service: RecognizerService):
    """
    Предсказывает стресс по данным ЭЭГ

        :param data_eeg: Данные ЭЭГ.
        :param data_mode: Режим полученных данных (сырые или отфильтрованные).
        :param recognizer_service: Сервис для распознавания стресса по ЭЭГ.
        :return: Список с предсказаниями.
    """
    return await recognizer_service.predict_stress(data_eeg, data_mode)
