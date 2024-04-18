from abc import ABC

from numpy import ndarray


class AbstractStressRepository(ABC):
    async def predict_stress(self, data: ndarray):
        ...
