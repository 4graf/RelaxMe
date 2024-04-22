from abc import ABC

from micro_services.backend.schemas.eeg_data import EEGData


class AbstractStressRepository(ABC):
    async def predict_stress(self, data: EEGData):
        ...
