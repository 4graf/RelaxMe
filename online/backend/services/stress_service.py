from numpy import ndarray

from online.backend.interfaces.services.abstract_stress_service import AbstractStressService
from online.backend.repositories.rest_api.stress_repository import StressRepository


class StressService(AbstractStressService):

    def __init__(self, stress_repo: StressRepository):
        """
        Инициализация сервиса для работы со стрессом.

            :param stress_repo: Репозиторий для работы со стрессом.
        """

        self.stress_repo = stress_repo

    async def predict_stress(self, data: ndarray):
        predictions = await self.stress_repo.predict_stress(data)

        return predictions
