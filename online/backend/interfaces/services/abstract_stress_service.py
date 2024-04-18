from abc import ABC, abstractmethod

from numpy import ndarray


class AbstractStressService(ABC):
    @abstractmethod
    async def predict_stress(self, data: ndarray):
        ...
