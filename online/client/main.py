# import asyncio
#
# from httpx import AsyncClient
#
# from online.client.EEG.services.EEG_device_service import EEGDeviceService
# from online.stress_recognizer.services.stress_recognizer_service import StressRecognizerService
# from online.stress_recognizer.util.constants import DataMode
#
# eeg_device_service = EEGDeviceService()
#
# # stress_recognizer_service = StressRecognizerService()
#
#
# async def do_predict():
#     eeg_device_service.start()
#
#     for _ in range(10):
#         await asyncio.sleep(5)
#         data = eeg_device_service.get_data(only_eeg=True)
#
#         # prediction = await stress_recognizer_service.predict_stress(data, DataMode.RAW)
#         async with AsyncClient() as client:
#             response = await client.post('http://localhost:3000/api/v1/stress/predict', json={'data': data.tolist()})
#             prediction = response.json()
#         print(prediction)
#
# asyncio.run(do_predict())

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


def get_y(x):
    # return x**2
    return np.sin(x)


x = [0.]
y = [get_y(x[-1])]
# y = [random.randint(1, 10)]

fig, axs = plt.subplots(8, 1, sharex=True)
lines = [ax.plot(x, y)[0] for ax in axs]


def update(frame):
    global axs

    new_x = x[-1] + 0.1
    x.append(new_x)
    # y.append(random.randint(1, 10))
    y.append(get_y(new_x))
    # new_y = [random.randint(1, 10) for _ in range(len(y))]
    for ax, line in zip(axs, lines):  # ToDo: Замерить время. При необходимости оптимизировать zip
        line.set_data(x, y)
        ax.relim()
        ax.autoscale_view()


anim = FuncAnimation(fig, update, frames=1)
plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
#
# fig, ax = plt.subplots()
# xdata, ydata = [], []
# ln, = plt.plot([], [], 'ro')
#
# def init():
#     ax.set_xlim(0, 2*np.pi)
#     ax.set_ylim(-1, 1)
#     return ln,
#
# def update(frame):
#     xdata.append(frame)
#     ydata.append(np.sin(frame))
#     ln.set_data(xdata, ydata)
#     return ln,
#
# ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
#                     init_func=init, blit=True)
# plt.show()
#
#
# from datetime import datetime
# from matplotlib import pyplot
# from matplotlib.animation import FuncAnimation
# from random import randrange
#
# x_data, y_data = [], []
# y_data2 = []
#
# figure = pyplot.figure()
# line, = pyplot.plot_date(x_data, y_data, '-')
# line2, = pyplot.plot_date(x_data, y_data, '-')
#
# def update(frame):
#     x_data.append(datetime.now())
#     y_data.append(randrange(0, 100))
#     y_data2.append(randrange(0, 100))
#
#     line.set_data(x_data, y_data)
#     line.set_data(x_data, y_data2)
#     figure.gca().relim()
#     figure.gca().autoscale_view()
#     return line, line2,
#
# animation = FuncAnimation(figure, update, interval=200)
#
# pyplot.show()

# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# from matplotlib import style
# style.use('fivethirtyeight')
#
# # fig = plt.figure()
# # ax1 = fig.add_subplot(1,1,1)
# fig, axs = plt.subplots(8, 1, sharex=True)
# xs = []
# ys = []
#
# def get_x():
#     for i in range(1000):
#         yield i
#
# xxx = get_x()
#
# def animate(i):
#
#     xs.append(next(xxx))
#     ys.append(randrange(0, 100))
#
#     # ax1.clear()
#     # ax1.plot(xs, ys)
#
#     for ax in axs:
#         ax.clear()
#         ax.plot(xs, ys)
#         fig.gca().relim()
#         fig.gca().autoscale_view()
#
# ani = animation.FuncAnimation(fig, animate, interval=100)
# plt.show()

