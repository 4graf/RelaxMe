"""
API-маршруты для управления всеми микро-сервисами приложения.
"""
import asyncio
from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from microservices.backend.api.dependencies.service import get_stress_service, get_user_service, get_eeg_service
from microservices.backend.api.dependencies.session import validate_token
from microservices.backend.interfaces.services.abstract_eeg_service import AbstractEEGService
from microservices.backend.interfaces.services.abstract_stress_service import AbstractStressService
from microservices.backend.interfaces.services.abstract_user_service import AbstractUserService
from microservices.backend.schemas.eeg import EEGData, EEGPredictRequest, EEGAdd
from microservices.backend.schemas.stress_prediction import StressPrediction

router = APIRouter()


@router.post("/predict", status_code=status.HTTP_200_OK)
async def predict_stress(eeg_predict: EEGPredictRequest,
                         stress_service: Annotated[AbstractStressService, Depends(get_stress_service)],
                         eeg_service: Annotated[AbstractEEGService, Depends(get_eeg_service)]
                         ) \
        -> StressPrediction:
    """
    Записывает данные ЭЭГ в базу данных и предсказывает стресс

        :param eeg_predict: Данные ЭЭГ.
        :param stress_service: Сервис для работы со стрессом по ЭЭГ.
        :param eeg_service: Сервис для работы с ЭЭГ.
        :return: Список с предсказаниями.
    """
    eeg_data = EEGData(data=eeg_predict.data)
    eeg_add = EEGAdd(user_id=eeg_predict.user_id,
                     state=0,
                     data=eeg_predict.data)

    prediction, _ = await asyncio.gather(stress_service.predict_stress(eeg_data=eeg_data),
                                         eeg_service.add_eeg(eeg_add=eeg_add))

    return prediction
