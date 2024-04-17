import json
import time

import pandas as pd
import torch
from httpx import Client
from scipy.stats import skew, kurtosis
from torch import nn
from torch.utils.data import DataLoader, Dataset, random_split
import mne
import os
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
import asyncio




# duration_in_seconds = 5
# data = board.get_current_board_data(int(sampling_rate * duration_in_seconds))
# time.sleep(5)
# data = board.get_current_board_data(250*5)

# eeg_data = data[eeg_channels, :]

# data = []
# start_time = time.time()
# print(start_time)
# # Получение данных в режиме онлайн
# while time.time() - start_time < 1:
#     record = board.get_current_board_data(250)  # Получение 250 отсчетов данных
#     # Обработка данных здесь
#     print(record)
#     data.append(record)
# print(time.time())
# print(data[-1].shape)
# print(data.shape)
# with open(r"C:\Users\Арсений\Desktop\records.txt", mode='w') as f:
#     # f.write(str(data[-1].tolist()))
#     f.write(str(data.tolist()))

# board.stop_stream()
# board.release_session()

class StressRecognitionNetwork(nn.Module):
    def __init__(self, input_size):
        super().__init__()
        self.flatten = nn.Flatten(1)
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(input_size, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 16),
            nn.ReLU(),
            nn.Linear(16, 2),
        )

    def forward(self, x):
        # x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits


eeg_data_queue = None
# nn = StressRecognitionNetwork(352)
# nn.load_state_dict(torch.load(r'C:\Проекты прогерские\Проекты PyCharm\MyRelax\best-model-parameters.pt'))


async def record_eeg():
    global eeg_data_queue
    while True:
        print('Запись ЭЭГ')
        # start_time = time.time()
        # time.sleep(5)
        await asyncio.sleep(5)
        # while (time.time() - start_time) < 5:
        data = board.get_current_board_data(250 * 5)
        data = board.get_board_data()
        eeg_data = data[eeg_channels, :]
        # eeg_data = data[0, :]
        # eeg_data_queue.append(eeg_data)
        eeg_data_queue = eeg_data
        print('Конец записи ЭЭГ')


async def send_eeg():
    while True:
        # print('Сплю 5 сек и отправляю')
        # await asyncio.sleep(5)
        if len(eeg_data_queue) == 0:
            print('Сплю секунду')
            await asyncio.sleep(1)
            continue
        data_to_send = eeg_data_queue.copy()
        del eeg_data_queue[:]  # Очищаем очередь
        # print('После очистки', len(eeg_data_queue))
        # print('Данные', len(data_to_send), data_to_send[-1].shape)
        # Отправка данных на другой сервис по API
        # response = requests.post('http://your-api-endpoint', json=data_to_send)
        with (open(r"C:\Перенос\Доки\Мага брат\Методология научных исследований\ВКР\Онлайн записи\data.txt", mode='a')
              as f):
            for data in data_to_send:
                # print(data.shape)
                # f.write(str(data[-1].tolist()))
                # f.write(str(data.shape))
                # f.write(str(data.tolist()))
                f.write(str(data.size))
        print("Data sent to API")


# def bci_df(file_path, skip_rows=4, sfreq=250):
#     df = pd.read_csv(file_path, skiprows=skip_rows, skipinitialspace=True)
#     step = 1 / sfreq
#     df['Time'] = np.arange(0, len(df) / 250, step)
#     cols_to_drop = [col for col in df.columns if not col.startswith('EXG') and col != 'Time']
#     df = df.drop(columns=cols_to_drop, axis=1)
#     return df

def bci_data_to_mne(data, ch_names, sfreq=250):
    info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=['eeg'] * len(ch_names), verbose=False)
    eeg = mne.io.RawArray(data=data, info=info, verbose=False)
    eeg = eeg.set_eeg_reference(verbose=False)
    return eeg


def filter_eeg(data, low_cutoff=1, high_cutoff=40):
    data_filt = data.copy()

    data_notched = mne.filter.notch_filter(
        data_filt.get_data(),
        Fs=data_filt.info["sfreq"],
        freqs=50,
        verbose=False
    )
    data_filt = mne.io.RawArray(data=data_notched, info=data_filt.info, verbose=False)

    data_filt.filter(l_freq=low_cutoff, h_freq=high_cutoff, method='iir', verbose=False)
    return data_filt


def extract_features(data, epoch_duration=1):
    eeg_epochs = mne.make_fixed_length_epochs(data, epoch_duration, verbose=False)

    psd_alpha = eeg_epochs.compute_psd(fmin=8, fmax=13, verbose=False)
    psd_beta = eeg_epochs.compute_psd(fmin=13, fmax=40, verbose=False)
    psd_alpha = psd_alpha.get_data()
    psd_beta = psd_beta.get_data()
    features = np.hstack((psd_alpha.reshape((psd_alpha.shape[0], -1)),
                          psd_beta.reshape((psd_beta.shape[0], -1))))

    # mean_powers = []
    for psd in (psd_alpha, psd_beta):
        mean_power = np.mean(psd, axis=2)
        # mean_powers.append(mean_power)
        median_power = np.median(psd, axis=2)
        std_power = np.std(psd, axis=2)
        # var_power = np.var(psd, axis=1)
        skewness_power = skew(psd, axis=2)
        kurtosis_power = kurtosis(psd, axis=2)

        features = np.hstack((features, mean_power, median_power, std_power, skewness_power, kurtosis_power))
        # names.append()

    # mean_powers = [a/b for a, b in ]
    # features = np.hstack((features, mean_powers))
    return features


async def send_features():
    global eeg_data_queue
    while True:
        if eeg_data_queue is None:
            print('Сплю секунду')
            await asyncio.sleep(1)
            continue
        data_to_send = np.array(eeg_data_queue)
        eeg_data_queue = None  # Очищаем очередь
        # data_to_send = bci_data_to_mne(data_to_send, ch_names=channel_names)
        # data_to_send = filter_eeg(data_to_send)
        # data_to_send = extract_features(data_to_send)
        with (open(r"C:\Перенос\Доки\Мага брат\Методология научных исследований\ВКР\Онлайн записи\data.txt", mode='a')
              as f):
            # for data in data_to_send:
            # print(type(json.dumps(data_to_send.tolist())))
            client = Client(base_url='http://localhost:8080/api/v1/stress_eeg')
            # predict = client.post('/predict', json=json.dumps(data_to_send.tolist()))
            predict = client.post('/predict', json=json.dumps({'data': data_to_send.tolist()}))
            f.write(str(predict))
                # print(nn(torch.Tensor(data)))


async def main():

    task1 = asyncio.create_task(record_eeg())
    # task2 = asyncio.create_task(send_eeg())
    task2 = asyncio.create_task(send_features())
    await task1
    await task2

if __name__ == "__main__":
    try:
        params = BrainFlowInputParams()
        params.serial_port = 'COM3'
        # board = BoardShim(BoardIds.CYTON_BOARD, params)
        board = BoardShim(BoardIds.SYNTHETIC_BOARD, params)
        board.prepare_session()

        sampling_rate = board.get_sampling_rate(BoardIds.CYTON_BOARD)
        print('Частота записи:', sampling_rate, 'Гц')

        channel_names = board.get_eeg_names(BoardIds.CYTON_BOARD)
        print('Имена каналов:', channel_names)

        eeg_channels = BoardShim.get_eeg_channels(BoardIds.CYTON_BOARD.value)
        print(eeg_channels)

        board.start_stream()

        asyncio.run(main())

    except BaseException as e:
        print('Exception')
        raise e
    finally:
        if board.is_prepared():
            board.stop_stream()
            board.release_session()
