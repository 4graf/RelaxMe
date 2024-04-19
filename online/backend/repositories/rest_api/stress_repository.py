from online.backend.interfaces.repositories.abstract_stress_repository import AbstractStressRepository
from online.backend.models.rest_api.eeg_data import EEGDataRest
from online.backend.repositories.base import BaseRestApiRepository
from online.backend.schemas.eeg_data import EEGData
from online.backend.settings import EndpointSettings

endpoint_settings = EndpointSettings()


class StressRepository(AbstractStressRepository, BaseRestApiRepository):
    base_endpoint = endpoint_settings.stress_service_endpoint

    async def predict_stress(self, eeg: EEGData):
        payload = EEGDataRest.model_validate(eeg)
        response = await self.post(url='predict', payload=payload)

        return response.json()
