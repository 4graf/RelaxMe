from microservices.backend.interfaces.repositories.abstract_stress_repository import AbstractStressRepository
from microservices.backend.interfaces.services.abstract_stress_service import AbstractStressService
from microservices.backend.repositories.rest_api.stress_repository import StressRepository
from microservices.backend.schemas.eeg_data import EEGData
from microservices.backend.schemas.stress_prediction import StressPrediction


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
