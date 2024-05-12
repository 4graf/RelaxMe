"""
API-маршруты для управления всеми микро-сервисами приложения.
"""
from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from microservices.backend.api.dependencies.service import get_stress_service
from microservices.backend.api.dependencies.session import validate_token
from microservices.backend.interfaces.services.abstract_stress_service import AbstractStressService
from microservices.backend.schemas.eeg_data import EEGData
from microservices.backend.schemas.stress_prediction import StressPrediction

router = APIRouter()


# @router.post("/predict", status_code=status.HTTP_200_OK)
# async def predict_stress(data_eeg: EEGData,
#                          stress_service: Annotated[AbstractStressService, Depends(get_stress_service)],
#                          current_user: Annotated[..., Depends(validate_token)]) \
#         -> StressPrediction:
#     """
#     Предсказывает стресс по данным ЭЭГ
#
#         :param data_eeg: Данные ЭЭГ.
#         :param stress_service: Сервис для работы со стрессом по ЭЭГ.
#         :return: Список с предсказаниями.
#     """
#     return await stress_service.predict_stress(data_eeg, current_user)
