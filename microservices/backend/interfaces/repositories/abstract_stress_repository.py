from abc import ABC, abstractmethod

from microservices.backend.schemas.eeg_data import EEGData


class AbstractStressRepository(ABC):
    @abstractmethod
    async def predict_stress(self, data: EEGData):
        ...
