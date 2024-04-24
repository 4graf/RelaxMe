from abc import ABC, abstractmethod

from microservices.backend.interfaces.repositories.abstract_stress_repository import AbstractStressRepository
from microservices.backend.schemas.eeg_data import EEGData


class AbstractStressService(ABC):
    stress_repo: AbstractStressRepository

    @abstractmethod
    async def predict_stress(self, data: EEGData):
        ...
