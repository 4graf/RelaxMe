import asyncio
import random

import matplotlib.pyplot as plt
import numpy as np
from httpx import AsyncClient

from microservices.client.EEG.services.EEG_device_service import EEGDeviceService

eeg_device_service = EEGDeviceService()


async def do_predict():
    eeg_device_service.start()

    count_channels = len(eeg_device_service.eeg_channels)
    x = [0]
    data_plot = [[0] for _ in range(count_channels)]

    fig, axs = plt.subplots(count_channels, 1, sharex=True, constrained_layout=True)
    fig.canvas.manager.set_window_title('RelaxMe')
    colors = plt.cm.jet(np.linspace(0, 1, count_channels))
    lines = []
    for ax, data, label, color in zip(axs, data_plot, eeg_device_service.channel_names, colors):
        lines.append(ax.plot(x, data, c=color)[0])
        # ax.set_title(label, loc='left', fontsize=10)

    fig.legend(labels=eeg_device_service.channel_names,
               loc="upper right")
    plt.ion()
    plt.show(block=False)

    x = np.arange(0, 60, 1 / eeg_device_service.sampling_rate).tolist()  # ToDo: добавить динамическую коррекцию х оси
    await asyncio.sleep(5)
    for _ in range(1, 25):
        # time.sleep(5)
        # await asyncio.sleep(5)

        plt.pause(1)
        data = eeg_device_service.get_data(only_eeg=True)
        payload = {
            'user_id': '608f1294-5c1d-49f1-85ee-f1fd2909fffb',
            'data': data.tolist()
        }

        async with AsyncClient() as client:
            response = await client.post('http://localhost:3000/api/v1/stress/predict', json=payload)
            prediction = response.json()

        # prediction = random.randint(0, 1)  # Mock-заглушка

        new_data_plot = data.tolist()
        predict_x_start = len(data_plot[0])
        # x.extend([x[-1] + (i / eeg_device_service.sampling_rate) for i in range(1, len(new_data_plot[0])+1)])
        for all_data_plot, new_data in zip(data_plot, new_data_plot):
            all_data_plot.extend(new_data)
        predict_x_stop = len(data_plot[0])

        predict_color = 'g' if prediction == 0 else 'r'

        for ax, line, data in zip(axs, lines, data_plot):  # ToDo: Замерить время. При необходимости оптимизировать zip
            line.set_data(x[:len(data)], data)

            ax.axvspan(x[predict_x_start], x[predict_x_stop], facecolor=predict_color, alpha=0.2)

            ax.relim()
            ax.autoscale_view()

            ax.draw_artist(ax.patch)
            ax.draw_artist(line)

        fig.canvas.update()
        fig.canvas.flush_events()


asyncio.run(do_predict())
#
#
#
# import asyncio
# import random
# from uuid import UUID
#
# import matplotlib.pyplot as plt
# import numpy as np
# from httpx import AsyncClient
#
# from microservices.client.EEG.services.EEG_device_service import EEGDeviceService
#
# eeg_device_service = EEGDeviceService()
#
#
# async def do_predict():
#     eeg_device_service.start()
#
#     await asyncio.sleep(5)
#     for _ in range(1, 25):
#         # time.sleep(5)
#         # await asyncio.sleep(5)
#
#         plt.pause(1)
#         data = eeg_device_service.get_data(only_eeg=True)
#         payload = {
#             'user_id': '608f1294-5c1d-49f1-85ee-f1fd2909fffb',
#             'state': 0,
#             'data': data.tolist()
#         }
#
#         async with AsyncClient() as client:
#
#             response = await client.post('http://localhost:3000/api/v1/eeg/add', json=payload)
#             print(response.json())
#
#
# asyncio.run(do_predict())
#
