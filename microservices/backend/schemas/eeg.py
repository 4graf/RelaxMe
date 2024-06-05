from datetime import datetime
from uuid import UUID

from microservices.backend.schemas.base import BaseSchema


class EEGData(BaseSchema):
    data: list


class EEG(BaseSchema):
    user_id: UUID
    state: int
    data: list


class EEGAdd(BaseSchema):
    user_id: UUID
    state: int
    data: list


class EEGPredictRequest(BaseSchema):
    user_id: UUID
    data: list


class EEGInfo(BaseSchema):
    added_at: datetime
    user_id: UUID
    state: int
    data: list
