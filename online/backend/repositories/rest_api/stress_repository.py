from numpy import ndarray

from online.backend.interfaces.repositories.abstract_stress_repository import AbstractStressRepository
from online.backend.repositories.base import BaseRestApiRepository
from online.backend.settings import EndpointSettings

endpoint_settings = EndpointSettings()


class StressRepository(AbstractStressRepository, BaseRestApiRepository):
    base_endpoint = endpoint_settings.stress_service_endpoint

    async def predict_stress(self, data: ndarray):
        response = await self.post(url='predict', payload=data)

        return response.json()
