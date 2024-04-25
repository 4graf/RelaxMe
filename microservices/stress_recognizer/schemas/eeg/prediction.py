from pydantic import BaseModel


class Prediction(BaseModel):
    labels: list[int]
