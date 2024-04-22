from micro_services.backend.interfaces.repositories.abstract_stress_repository import AbstractStressRepository
from micro_services.backend.interfaces.services.abstract_stress_service import AbstractStressService
from micro_services.backend.repositories.rest_api.stress_repository import StressRepository
from micro_services.backend.schemas.eeg_data import EEGData
from micro_services.backend.schemas.stress_prediction import StressPrediction


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
