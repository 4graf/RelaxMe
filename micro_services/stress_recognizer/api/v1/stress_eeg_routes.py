"""
Модуль предоставляет API-маршруты для работы со стрессом по ЭЭГ с помощью нейросети.
"""
from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from micro_services.stress_recognizer.api.dependencies import get_recognizer_stress_service
from micro_services.stress_recognizer.schemas.eeg.prediction import Prediction
from micro_services.stress_recognizer.schemas.eeg.raw_eeg import RawEEG
from micro_services.stress_recognizer.services.stress_recognizer_service import StressRecognizerService
from micro_services.stress_recognizer.util.constants import DataMode

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
