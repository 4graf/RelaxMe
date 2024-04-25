"""
Модуль предоставляет API-маршруты для работы со стрессом по ЭЭГ с помощью нейросети.
"""
from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from microservices.stress_recognizer.api.dependencies import get_recognizer_stress_service
from microservices.stress_recognizer.schemas.eeg.prediction import Prediction
from microservices.stress_recognizer.schemas.eeg.raw_eeg import RawEEG
from microservices.stress_recognizer.services.stress_recognizer_service import StressRecognizerService
from microservices.stress_recognizer.util.constants import DataMode

router = APIRouter()


@router.post("/predict", status_code=status.HTTP_200_OK)
async def predict_stress(data_eeg: RawEEG,
                         recognizer_service: Annotated[StressRecognizerService, Depends(get_recognizer_stress_service)]) \
        -> Prediction:
    """
    Предсказывает стресс по данным ЭЭГ

        :param data_eeg: Данные ЭЭГ.
        :param recognizer_service: Сервис для распознавания стресса по ЭЭГ.
        :return: Список с предсказаниями.
    """
    return await recognizer_service.predict_stress(data_eeg, DataMode.RAW)
