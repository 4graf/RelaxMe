from abc import ABC, abstractmethod

from microservices.backend.interfaces.repositories.abstract_eeg_repository import AbstractEEGRepository
from microservices.backend.schemas.eeg import EEGAdd


class AbstractEEGService(ABC):
    eeg_repo: AbstractEEGRepository

    @abstractmethod
    async def add_eeg(self, eeg_add: EEGAdd):
        ...
