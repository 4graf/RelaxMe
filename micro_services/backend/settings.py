from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class EndpointSettings(BaseSettings):
    stress_service_endpoint: str
