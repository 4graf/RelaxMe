from online.backend.interfaces.services.abstract_stress_service import AbstractStressService


class StressService(AbstractStressService):
    def __init__(self, stress_repo: StressRepository):
        """
        Инициализация сервиса для работы со стрессом.

            :param stress_repo: Репозиторий для работы со стрессом.
        """

        self.stress_repo = stress_repo

