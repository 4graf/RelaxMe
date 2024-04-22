import asyncio
import time
from datetime import datetime

from httpx import AsyncClient

from online.client.EEG.services.EEG_device_service import EEGDeviceService
from online.stress_recognizer.services.stress_recognizer_service import StressRecognizerService
from online.stress_recognizer.util.constants import DataMode

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


eeg_device_service = EEGDeviceService()

# stress_recognizer_service = StressRecognizerService()


async def do_predict():
    eeg_device_service.start()

    x = [0]
    data_plot = [[0] for _ in range(2)]


    fig, axs = plt.subplots(2, 1, sharex=True)
    lines = [ax.plot(x, data)[0] for ax, data in zip(axs, data_plot)]
    plt.ion()
    plt.show(block=False)

    def update(frame):


        # new_x = np.arange(x[-1], datetime.now(), 1/250).tolist()
        new_x = [x[-1] + ((i+1) * 0.004) for i in range(len(new_data_plot[0]))]
        x.extend(new_x)
        for i in range(2):
            data_plot[i].extend(new_data_plot[i])
            lines[i].set_data(x, data_plot[i])
            axs[i].relim()
            axs[i].autoscale_view()

        print('new draw')

        # for ax, line in zip(axs, lines):  # ToDo: Замерить время. При необходимости оптимизировать zip
        #     line.set_data(x, y)
        #     ax.relim()
        #     ax.autoscale_view()

    # x.extend([2, 3, 4, 5])
    # data_plot[0].extend([1, 3, 2, 7])
    # data_plot[1].extend([1, 1, 2, 10])

    # for ax, line, data in zip(axs, lines, data_plot):  # ToDo: Замерить время. При необходимости оптимизировать zip
    #     line.set_data(x, data)
    #     ax.draw_artist(ax.patch)
    #     ax.draw_artist(line)
    #     fig.canvas.update()
    #     fig.canvas.flush_events()
    #     ax.relim()
    #     ax.autoscale_view()

    # anim = FuncAnimation(fig, update, interval=1000)
    # plt.draw()
    last_x = 0
    for j in range(1, 10000000):
        # time.sleep(5)
        # await asyncio.sleep(5)
        # data = eeg_device_service.get_data(only_eeg=True)

        plt.pause(1)
        data = eeg_device_service.get_data(only_eeg=True)

        # data = np.random.rand(2, 10)
        new_data_plot = data.copy().tolist()[:2]
        print('new data')
        x.extend([last_x + (0.004*i) for i in range(1, len(new_data_plot[0])+1)])
        last_x = x[-1]
        data_plot[0].extend(new_data_plot[0])
        data_plot[1].extend(new_data_plot[1])


        for ax, line, data in zip(axs, lines, data_plot):  # ToDo: Замерить время. При необходимости оптимизировать zip
            line.set_data(x, data)

            ax.relim()
            ax.autoscale_view()

            ax.draw_artist(ax.patch)
            ax.draw_artist(line)

            fig.canvas.update()
            fig.canvas.flush_events()
        # plt.pause(1)

    # for _ in range(10):
    #     await asyncio.sleep(1)
    #     # data = eeg_device_service.get_data(only_eeg=True)
    #     data = np.random.rand(2, 10)
    #     new_data_plot = data.copy().tolist()[:2]
    #     print(anim.new_frame_seq())

        # prediction = await stress_recognizer_service.predict_stress(data, DataMode.RAW)
        # async with AsyncClient() as client:
        #     response = await client.post('http://localhost:3000/api/v1/stress/predict', json={'data': data.tolist()})
        #     prediction = response.json()
        # print(prediction)

asyncio.run(do_predict())


# def get_y(x):
#     # return x**2
#     return np.sin(x)


# x = [0.]
# y = [get_y(x[-1])]
# y = [random.randint(1, 10)]

# fig, axs = plt.subplots(8, 1, sharex=True)
# lines = [ax.plot(x, y)[0] for ax in axs]


# def update(frame):
#     global axs
#
#     new_x = x[-1] + 0.1
#     x.append(new_x)
#     # y.append(random.randint(1, 10))
#     y.append(get_y(new_x))
#     # new_y = [random.randint(1, 10) for _ in range(len(y))]
#     for ax, line in zip(axs, lines):  # ToDo: Замерить время. При необходимости оптимизировать zip
#         line.set_data(x, y)
#         ax.relim()
#         ax.autoscale_view()
#
#
# anim = FuncAnimation(fig, update, frames=1)
# plt.show()


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

