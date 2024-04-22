from abc import ABC, abstractmethod

from micro_services.backend.interfaces.repositories.abstract_stress_repository import AbstractStressRepository
from micro_services.backend.schemas.eeg_data import EEGData


class AbstractStressService(ABC):
    stress_repo: AbstractStressRepository

    @abstractmethod
    async def predict_stress(self, data: EEGData):
        ...
