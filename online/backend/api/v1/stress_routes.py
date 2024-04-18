"""
Модуль предоставляет API-маршруты для управления поставщиками.
"""
from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from online.stress_recognizer.api.dependencies import get_recognizer_stress_service
from online.stress_recognizer.schemas.eeg.prediction import Prediction
from online.stress_recognizer.schemas.eeg.raw_eeg import RawEEG
from online.stress_recognizer.services.stress_recognizer_service import StressRecognizerService
from online.stress_recognizer.util.constants import DataMode

router = APIRouter()


@router.post("/predict", status_code=status.HTTP_200_OK)
async def predict_stress(data_eeg: RawEEG,
                         stress_service: Annotated[StressService, Depends(get_stress_service)]) \
        -> list[Prediction]:
    """
    Предсказывает стресс по данным ЭЭГ

        :param data_eeg: Данные ЭЭГ.
        :param stress_service: Сервис для работы со стрессом по ЭЭГ.
        :return: Список с предсказаниями.
    """
    return await stress_service.predict_stress(data_eeg, DataMode.RAW)
