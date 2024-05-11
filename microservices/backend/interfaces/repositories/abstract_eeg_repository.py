from abc import ABC, abstractmethod

from microservices.backend.schemas.eeg_data import EEGData


class AbstractEEGRepository(ABC):
    @abstractmethod
    async def add_eeg(self, data: EEGData):
        ...
