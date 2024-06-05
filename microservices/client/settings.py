from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class EndpointSettings(BaseSettings):
    eeg_service_endpoint: str
    eeg_interval: int
    stress_service_endpoint: str
