from microservices.backend.schemas.base import BaseSchema


class StressPrediction(BaseSchema):
    labels: list[int]
