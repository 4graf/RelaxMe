from abc import ABC

from httpx import Client


class BaseRestApiRepository(ABC):
    def __init__(self, client: Client):
        self.client = client



# client = Client(base_url='http://localhost:8080/api/v1/stress_eeg')
