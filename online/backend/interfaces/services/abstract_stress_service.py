from abc import ABC, abstractmethod
from enum import Enum

from numpy import ndarray


class AbstractStressService(ABC):
    @abstractmethod
    async def predict_stress(self, data: ndarray, data_mode: Enum):
        ...
