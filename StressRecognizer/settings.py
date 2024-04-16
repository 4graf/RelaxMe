import os
from dotenv import load_dotenv


load_dotenv()


class NNSettings:
    nn_weights_path = os.getenv('NN_WEIGHTS_PATH')
    nn_features_count = os.getenv('NN_FEATURES_COUNT')


class EEGSettings:
    sfreq = os.getenv('SFREQ')
    eeg_channel_names = os.getenv('EEG_CHANNEL_NAMES')
    low_cutoff = os.getenv('LOW_CUTOFF')
    high_cutoff = os.getenv('HIGH_CUTOFF')
    epoch_duration = os.getenv('EPOCH_DURATION')
