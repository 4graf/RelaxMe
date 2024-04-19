from pydantic import BaseModel


class PredictionRest(BaseModel):
    labels: list[int]
