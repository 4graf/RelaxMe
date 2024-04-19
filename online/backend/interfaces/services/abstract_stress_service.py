from abc import ABC, abstractmethod

from online.backend.interfaces.repositories.abstract_stress_repository import AbstractStressRepository
from online.backend.schemas.eeg_data import EEGData


class AbstractStressService(ABC):
    stress_repo: AbstractStressRepository

    @abstractmethod
    async def predict_stress(self, data: EEGData):
        ...
