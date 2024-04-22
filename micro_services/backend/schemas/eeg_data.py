from pydantic import BaseModel


class EEGData(BaseModel):
    data: list
