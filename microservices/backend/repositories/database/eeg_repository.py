from microservices.backend.interfaces.repositories.abstract_eeg_repository import AbstractEEGRepository
from microservices.backend.models.rest_api.eeg_data import EEGDataRest
from microservices.backend.models.rest_api.prediction import PredictionRest
from microservices.backend.repositories.database.base import BaseDBRepository
from microservices.backend.schemas.eeg_data import EEGData
from microservices.backend.schemas.stress_prediction import StressPrediction


class EEGRepository(AbstractEEGRepository, BaseDBRepository):
    # model = EEGModel

    async def add_eeg(self, eeg: EEGData) -> ...:
        # payload = EEGDataRest.model_validate(eeg.model_dump())
        # response = await self.post(url='predict', payload=payload.model_dump())
        # prediction_rest = PredictionRest.model_validate(response.json())
        # prediction = StressPrediction.model_validate(prediction_rest.model_dump())
        # return prediction

