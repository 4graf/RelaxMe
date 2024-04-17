from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class NNSettings(BaseSettings):
    nn_weights_path: str
    nn_features_count: int


class EEGSettings(BaseSettings):
    sfreq: int
    eeg_channel_names: tuple
    low_cutoff: int
    high_cutoff: int
    epoch_duration: int
