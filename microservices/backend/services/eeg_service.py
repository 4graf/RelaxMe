from microservices.backend.interfaces.repositories.abstract_eeg_repository import AbstractEEGRepository
from microservices.backend.interfaces.services.abstract_eeg_service import AbstractEEGService
from microservices.backend.schemas.eeg import EEGAdd, EEG


class EEGService(AbstractEEGService):
    eeg_repo: AbstractEEGRepository

    def __init__(self, eeg_repo: AbstractEEGRepository):
        """
        Инициализация сервиса для работы с ЭЭГ.

            :param eeg_repo: Репозиторий для работы с ЭЭГ.
        """

        self.eeg_repo = eeg_repo

    async def add_eeg(self, eeg_add: EEGAdd) -> None:
        eeg = EEG(user_id=eeg_add.user_id,
                  state=eeg_add.state,
                  data=eeg_add.data)
        await self.eeg_repo.add_eeg(eeg)
