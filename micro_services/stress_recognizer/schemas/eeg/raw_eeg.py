from pydantic import BaseModel


class RawEEG(BaseModel):
    data: list
