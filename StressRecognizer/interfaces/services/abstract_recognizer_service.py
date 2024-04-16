from abc import ABC, abstractmethod

from numpy import ndarray


class AbstractRecognizerService(ABC):
    @abstractmethod
    async def extract_features(self, data: ndarray):
        ...

    @abstractmethod
    async def predict_stress(self, data: ndarray):
        ...
