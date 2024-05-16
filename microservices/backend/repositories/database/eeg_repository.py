from microservices.backend.interfaces.repositories.abstract_eeg_repository import AbstractEEGRepository
from microservices.backend.models.database import EEGModel
from microservices.backend.repositories.database.base import BaseDBRepository
from microservices.backend.schemas.eeg import EEG, EEGInfo


class EEGRepository(AbstractEEGRepository, BaseDBRepository):
    model = EEGModel

    async def add_eeg(self, eeg: EEG) -> None:
        await self._add(eeg.model_dump())

    async def get_all_eeg(self) -> list[EEGInfo]:
        all_eeg = await self._get_all()
        all_eeg = [EEGInfo.model_validate(eeg) for eeg in all_eeg]
        return all_eeg
