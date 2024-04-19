from numpy import ndarray

from online.backend.interfaces.repositories.abstract_stress_repository import AbstractStressRepository
from online.backend.interfaces.services.abstract_stress_service import AbstractStressService
from online.backend.repositories.rest_api.stress_repository import StressRepository
from online.backend.schemas.eeg_data import EEGData
from online.backend.schemas.stress_prediction import StressPrediction


class StressService(AbstractStressService):
    stress_repo: AbstractStressRepository

    def __init__(self, stress_repo: StressRepository):
        """
        Инициализация сервиса для работы со стрессом.

            :param stress_repo: Репозиторий для работы со стрессом.
        """

        self.stress_repo = stress_repo

    async def predict_stress(self, eeg: EEGData) -> StressPrediction:
        prediction = await self.stress_repo.predict_stress(eeg)

        return prediction
