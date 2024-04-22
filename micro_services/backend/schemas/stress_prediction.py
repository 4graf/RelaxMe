from pydantic import BaseModel


class StressPrediction(BaseModel):
    labels: list[int]
