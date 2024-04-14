import time
import torch
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

eeg_data_queue = []


async def record_eeg():
    while True:
        print('Запись ЭЭГ')
        # start_time = time.time()
        # time.sleep(5)
        await asyncio.sleep(5)
        # while (time.time() - start_time) < 5:
        data = board.get_current_board_data(250 * 5)
        data = board.get_board_data()
        # eeg_data = data[eeg_channels, :]
        eeg_data = data[0, :]
        eeg_data_queue.append(eeg_data)
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


async def main():

    task1 = asyncio.create_task(record_eeg())
    task2 = asyncio.create_task(send_eeg())
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
