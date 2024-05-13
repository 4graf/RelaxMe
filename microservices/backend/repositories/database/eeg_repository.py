from microservices.backend.interfaces.repositories.abstract_eeg_repository import AbstractEEGRepository
from microservices.backend.models.database import EEGModel
from microservices.backend.repositories.database.base import BaseDBRepository
from microservices.backend.schemas.eeg import EEG


class EEGRepository(AbstractEEGRepository, BaseDBRepository):
    model = EEGModel

    async def add_eeg(self, eeg: EEG) -> None:
        await self._add(eeg.model_dump())
