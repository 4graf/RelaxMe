from pydantic import BaseModel


class StressPrediction(BaseModel):
    prediction: list[int]
