# from pyOpenBCI import OpenBCICyton
# import time
#
# def handle_sample(sample):
#     # Обработка данных с устройства OpenBCI
#     print(sample.channels_data)
#
# # Подключение к устройству OpenBCI
# board = OpenBCICyton(port='/dev/ttyUSB0', daisy=False)  # Укажите соответствующий порт
#
# # Начало сбора данных
# board.start_streaming(handle_sample)
#
# # В течение 10 секунд будут выводиться данные с устройства
# time.sleep(10)
#
# # Остановка сбора данных
# board.stop_streaming()
import time

from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds

# Установка параметров для OpenBCI
params = BrainFlowInputParams()
params.serial_port = 'COM3'  # Укажите порт, к которому подключено ваше устройство OpenBCI

# Создание экземпляра BoardShim и подключение к устройству OpenBCI
board = BoardShim(BoardIds.CYTON_BOARD, params)
board.prepare_session()

# Получение частоты записи
sampling_rate = board.get_sampling_rate(BoardIds.CYTON_BOARD)
print('Частота записи:', sampling_rate, 'Гц')

# Получение имен каналов
channel_names = board.get_eeg_names(BoardIds.CYTON_BOARD)
print('Имена каналов:', channel_names)

# Начало сбора данных
board.start_stream()

duration_in_seconds = 5
# data = board.get_current_board_data(int(sampling_rate * duration_in_seconds))
time.sleep(5)
data = board.get_current_board_data(250*5)

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
print(data.shape)
with open(r"C:\Users\Арсений\Desktop\records.txt", mode='w') as f:
    # f.write(str(data[-1].tolist()))
    f.write(str(data.tolist()))

# Завершение сеанса сбора данных
board.stop_stream()
board.release_session()
