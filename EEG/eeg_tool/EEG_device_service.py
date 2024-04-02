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

# Начало сбора данных
board.start_stream()

data = []
start_time = time.time()
print(start_time)
# Получение данных в режиме онлайн
while time.time() - start_time < 1:
    record = board.get_current_board_data(256)  # Получение 256 отсчетов данных
    # Обработка данных здесь
    data.append(record)
print(time.time())
print(data[-1].shape)
with open(r"C:\Users\Арсений\Desktop\records.txt", mode='w') as f:
    f.write(str(data[-1].tolist()))

# Завершение сеанса сбора данных
board.stop_stream()
board.release_session()
