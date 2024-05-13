from abc import ABC, abstractmethod

from microservices.backend.schemas.eeg import EEG


class AbstractEEGRepository(ABC):
    @abstractmethod
    async def add_eeg(self, data: EEG):
        ...
