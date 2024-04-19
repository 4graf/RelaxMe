from online.backend.interfaces.repositories.abstract_stress_repository import AbstractStressRepository
from online.backend.models.rest_api.eeg_data import EEGDataRest
from online.backend.models.rest_api.prediction import PredictionRest
from online.backend.repositories.base import BaseRestApiRepository
from online.backend.schemas.eeg_data import EEGData
from online.backend.schemas.stress_prediction import StressPrediction
from online.backend.settings import EndpointSettings

endpoint_settings = EndpointSettings()


class StressRepository(AbstractStressRepository, BaseRestApiRepository):
    base_endpoint = endpoint_settings.stress_service_endpoint

    async def predict_stress(self, eeg: EEGData) -> StressPrediction:
        payload = EEGDataRest.model_validate(eeg.model_dump())
        response = await self.post(url='predict', payload=payload.model_dump())
        prediction_rest = PredictionRest.model_validate(response.json())
        prediction = StressPrediction.model_validate(prediction_rest.model_dump())
        return prediction
