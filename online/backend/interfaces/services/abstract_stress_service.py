from abc import ABC, abstractmethod

from numpy import ndarray

from online.backend.interfaces.repositories.abstract_stress_repository import AbstractStressRepository


class AbstractStressService(ABC):
    stress_repo: AbstractStressRepository

    @abstractmethod
    async def predict_stress(self, data: ndarray):
        ...
