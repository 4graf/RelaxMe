from pydantic import BaseModel


class EEGDataRest(BaseModel):
    data: list
    # data_mode: str
