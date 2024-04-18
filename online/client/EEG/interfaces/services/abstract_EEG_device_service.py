from abc import ABC, abstractmethod
from enum import Enum

from numpy import ndarray


class AbstractEEGDeviceService(ABC):
    @abstractmethod
    def start(self):
        ...

    @abstractmethod
    def get_data(self, only_eeg=False, **kwargs):
        ...

    @abstractmethod
    def get_data_async(self, **kwargs):
        ...

    @abstractmethod
    def stop(self):
        ...
