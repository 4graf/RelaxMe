"""
Модуль предоставляет API-маршруты для управления поставщиками.
"""
from typing import Any, Annotated

from fastapi import APIRouter, Depends
from starlette import status

from stress_recognizer.api.dependencies import get_recognizer_stress_service
from stress_recognizer.schemas.eeg.prediction import Prediction
from stress_recognizer.schemas.eeg.raw_eeg import RawEEG
from stress_recognizer.services.recognizer_service import RecognizerService
from stress_recognizer.util.constants import DataMode

router = APIRouter()


@router.post("/predict", status_code=status.HTTP_200_OK)
async def predict_stress(data_eeg: RawEEG,
                         recognizer_service: Annotated[RecognizerService, Depends(get_recognizer_stress_service)]) \
        -> list[Prediction]:
    """
    Предсказывает стресс по данным ЭЭГ

        :param data_eeg: Данные ЭЭГ.
        :param data_mode: Режим полученных данных (сырые или отфильтрованные).
        :param recognizer_service: Сервис для распознавания стресса по ЭЭГ.
        :return: Список с предсказаниями.
    """
    return await recognizer_service.predict_stress(data_eeg, DataMode.RAW)
