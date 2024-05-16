from abc import ABC, abstractmethod

from microservices.backend.interfaces.repositories.abstract_eeg_repository import AbstractEEGRepository
from microservices.backend.schemas.eeg import EEGAdd, EEGInfo


class AbstractEEGService(ABC):
    eeg_repo: AbstractEEGRepository

    @abstractmethod
    async def add_eeg(self, eeg_add: EEGAdd):
        ...

    @abstractmethod
    async def get_all_eeg(self) -> list[EEGInfo]:
        ...
