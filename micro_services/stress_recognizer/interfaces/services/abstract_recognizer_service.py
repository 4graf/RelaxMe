from abc import ABC, abstractmethod
from enum import Enum

from numpy import ndarray


class AbstractRecognizerService(ABC):
    @abstractmethod
    async def extract_features(self, data: ndarray, data_mode: Enum):
        ...

    @abstractmethod
    async def predict_stress(self, data: ndarray, data_mode: Enum):
        ...
