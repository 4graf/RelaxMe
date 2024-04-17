from pydantic import BaseModel


class Prediction(BaseModel):
    label: int
