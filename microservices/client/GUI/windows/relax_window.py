# import matplotlib
# import matplotlib.pyplot as plt
# import mne
# import numpy as np
import json

from PySide6.QtCore import QTimer, QUrl, QByteArray
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QPushButton

from microservices.client.EEG.services.EEG_device_service import EEGDeviceService
from microservices.client.GUI.windows.ui_relax_window import Ui_RelaxWindow
from microservices.client.GUI.windows.video_window import get_video_widget
from microservices.client.settings import EndpointSettings

# from matplotlib.backends.backend_qtagg import (FigureCanvasQTAgg as FigureCanvas,
#                                                NavigationToolbar2QT as NavigationToolbar)

# from classification import EEGClassifier
# from preprocessing import EEGPreprocessing


# matplotlib.use('Qt5Agg')
# mne.viz.set_browser_backend('qt')

settings = EndpointSettings()


class RelaxWindow(QMainWindow):
    def __init__(self, video_urls, eeg_device_service: EEGDeviceService = None):
        super(RelaxWindow, self).__init__()
        self.ui = Ui_RelaxWindow()
        self.ui.setupUi(self)

        self.eeg_device_service = eeg_device_service

        self._size_grid = (3, 3)
        self.video_btns = {}
        self.video_urls = video_urls

        self.all_video_show()

        self.ui.back_button.clicked.connect(self.back_to_menu)

        if self.eeg_device_service:
            self.manager = QNetworkAccessManager()
            self.manager.finished.connect(self.api_reply)

            self.timer = QTimer()
            self.timer.setInterval(settings.eeg_interval)
            self.timer.timeout.connect(self.api_predict)

            # self.timer.timeout.connect(lambda: asyncio.ensure_future(self.predict_stress()))

        self.showMaximized()

    def api_predict(self):
        request = QNetworkRequest(QUrl(f"{settings.stress_service_endpoint}/predict"))
        request.setHeader(QNetworkRequest.KnownHeaders.ContentTypeHeader, "application/json")

        data = self.eeg_device_service.get_data(only_eeg=True)
        payload = {
            'user_id': '608f1294-5c1d-49f1-85ee-f1fd2909fffb',
            'data': data.tolist()
        }
        body = QByteArray()
        body.append(json.dumps(payload).encode("utf-8"))

        self.manager.post(request, body)

    def api_reply(self, reply: QNetworkReply):
        print(reply.readAll().data().decode('utf8'))

    def all_video_show(self) -> None:
        self.ui.content_widget.setCurrentIndex(0)

        self.video_btns = {}

        for i, url in enumerate(self.video_urls):
            layout = QVBoxLayout(self)
            video = get_video_widget(url, start=300, autoplay=True, mute=True)
            btn = QPushButton(text='Смотреть')
            btn.clicked.connect(self.open_video)
            layout.addWidget(video)
            layout.addWidget(btn)

            self.video_btns[id(btn)] = url

            self.ui.video_grid_layout.addLayout(layout,
                                                i // self._size_grid[0],
                                                i % self._size_grid[1])

    def open_video(self):
        btn = self.sender()
        self._clear_children(self.ui.video_grid_layout)

        video = get_video_widget(self.video_btns[id(btn)], autoplay=True, mute=True)
        self.ui.player_video_layout.addWidget(video)
        self.ui.content_widget.setCurrentIndex(1)

        self.eeg_device_service.start()
        self.timer.start()

    def back_to_menu(self):
        self._clear_children(self.ui.player_video_layout)
        self.all_video_show()

        self.timer.stop()
        self.eeg_device_service.stop()

    @classmethod
    def _clear_children(cls, parent):
        while parent.count():
            child = parent.takeAt(0)
            child_widget = child.widget()
            if child_widget:
                child_widget.setParent(None)
                child_widget.deleteLater()
            elif child:
                cls._clear_children(child)
