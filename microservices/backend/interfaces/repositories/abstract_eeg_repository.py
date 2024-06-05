from abc import ABC, abstractmethod

from microservices.backend.schemas.eeg import EEG, EEGInfo


class AbstractEEGRepository(ABC):
    @abstractmethod
    async def add_eeg(self, data: EEG):
        ...

    @abstractmethod
    async def get_all_eeg(self) -> list[EEGInfo]:
        ...
