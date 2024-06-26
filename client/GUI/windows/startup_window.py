import json
import sys

from PySide6.QtCore import QUrl, QFileInfo, QTimer, QByteArray, QPoint
from PySide6.QtGui import QCloseEvent, QColor
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PySide6.QtWidgets import QApplication, QRadioButton, QButtonGroup, QMessageBox, QGraphicsDropShadowEffect
from PySide6.QtWidgets import QMainWindow
from brainflow import BrainFlowError

from client.EEG.services.EEG_device_service import EEGDeviceService
from client.GUI.utils import QUESTIONARY
from client.GUI.windows.relax_window import RelaxWindow
from client.GUI.windows.themes import ThemeGUI
from client.GUI.windows.ui_startup_window import Ui_StartupWindow
from client.safe_place.safe_place import SafePlaceDecider
from client.settings import EndpointSettings

settings = EndpointSettings()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_StartupWindow()
        self.ui.setupUi(self)

        effect = QGraphicsDropShadowEffect(self)
        effect.setOffset(QPoint(0, 6))
        effect.setBlurRadius(50)
        effect.setColor(QColor("#C0AEE2"))
        self.ui.header_frame.setGraphicsEffect(effect)

        # self.eeg_device_service = None
        try:
            self.eeg_device_service = EEGDeviceService()
        except BrainFlowError:
            self.eeg_device_service = None

        self.stress_video_window = None
        self.relax_window = None
        self.survey_window = None
        self.player = None

        self.questionary = QUESTIONARY
        self.questionary_results = None
        self.questionary_current_id = -1
        self.quest_button_group = None
        self.safe_places = []

        self.ui.start_btn.clicked.connect(self.start_relax)
        self.ui.stress_video_btn.clicked.connect(self.open_stress_video)
        self.ui.testing_btn.clicked.connect(self.survey_show)
        self.ui.pushButton.clicked.connect(self.survey_next)
        self.ui.instruction_back_btn.clicked.connect(self.startup_show)
        self.ui.pushButton_2.clicked.connect(self.startup_show)
        self.ui.instruction_btn.clicked.connect(self.instruction_show)

        if self.eeg_device_service:
            self.manager = QNetworkAccessManager()
            self.manager.finished.connect(self.api_reply)

            self.timer = QTimer()
            self.timer.setInterval(settings.eeg_interval)
            self.timer.timeout.connect(self.api_send)

        self.auth_show()
        # self.showMaximized()

    def api_send(self):
        request = QNetworkRequest(QUrl(f"{settings.eeg_service_endpoint}/add"))
        request.setHeader(QNetworkRequest.KnownHeaders.ContentTypeHeader, "application/json")

        data = self.eeg_device_service.get_data(only_eeg=True)
        payload = {
            'user_id': '608f1294-5c1d-49f1-85ee-f1fd2909fffb',
            'state': 1,
            'data': data.tolist()
        }
        body = QByteArray()
        body.append(json.dumps(payload).encode("utf-8"))

        self.manager.post(request, body)

    def api_reply(self, reply: QNetworkReply):
        print(reply.readAll().data().decode('utf8'))

    def start_relax(self):
        if not self.relax_window or not self.relax_window.isVisible():
            self.relax_window = RelaxWindow(self.safe_places, self.eeg_device_service)
            self.relax_window.show()

    def open_stress_video(self):
        if not self.stress_video_window or not self.stress_video_window.isVisible():
            self.player = QMediaPlayer()
            self.player.setSource(QUrl.fromLocalFile(QFileInfo('../video/Stress video.mp4').absoluteFilePath()))
            self.stress_video_window = QVideoWidget()
            self.audio_output = QAudioOutput()
            self.player.setAudioOutput(self.audio_output)
            self.player.setVideoOutput(self.stress_video_window)
            self.stress_video_window.setWindowTitle('RelaxMe - Стресс-видео')
            self.stress_video_window.show()

            if self.eeg_device_service:
                self.timer.start()
                self.eeg_device_service.start()

            self.player.play()

            self.player.mediaStatusChanged.connect(self.player_status_changed)

    def player_status_changed(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            if self.eeg_device_service:
                self.timer.stop()
                self.eeg_device_service.stop()

            self.stress_video_window.close()

        # if not self.stress_video_window or not self.stress_video_window.isVisible():
        #     self.stress_video_window = VideoWindow(stress_video_id)
        #     self.stress_video_window.show()

    def survey_next(self):
        if self.questionary_current_id != -1:
            self.questionary_results.append({'question': self.questionary[self.questionary_current_id]['question'],
                                             'answer': self.quest_button_group.checkedId()})
            # self.questionary_results.append(self.group_box.checkedId())
            print(self.questionary_results)
        if self.questionary_current_id == len(self.questionary) - 1:
            self.questionary_current_id = -1
            self.survey_end_show()
            res = SafePlaceDecider.get_safe_place([item['answer'] for item in self.questionary_results])
            print(res)
            self.safe_places = SafePlaceDecider.all_places[tuple(res.items())]
            print(self.safe_places)

            self.startup_show()
        else:
            self.questionary_current_id += 1

            self.quest_button_group = QButtonGroup(self.ui.testing_page)

            data = self.questionary[self.questionary_current_id]

            self.ui.question_label.setText(data['question'])
            self._clear_children(self.ui.verticalLayout_4)
            for i, answer in enumerate(data['answers']):
                radio_btn = QRadioButton(answer, self.ui.testing_page)
                self.ui.verticalLayout_4.addWidget(radio_btn)
                self.quest_button_group.addButton(radio_btn, i)

    def make_light_theme(self):
        if self.ui.light_theme_action.isChecked():
            self.setStyleSheet(ThemeGUI.LIGHT)
            self.ui.dark_theme_action.setChecked(False)
        else:
            self.ui.light_theme_action.setChecked(True)

    def make_dark_theme(self):
        if self.ui.dark_theme_action.isChecked():
            self.setStyleSheet(ThemeGUI.DARK)
            self.ui.light_theme_action.setChecked(False)
        else:
            self.ui.dark_theme_action.setChecked(True)

    def auth_show(self) -> None:
        self.ui.content_widget.setCurrentIndex(0)

    def startup_show(self) -> None:
        self.ui.content_widget.setCurrentIndex(1)

    def survey_show(self):
        self.questionary_results = []

        self.survey_instruction_show()

        self.survey_next()
        self.ui.content_widget.setCurrentIndex(2)

    def instruction_show(self):
        self.ui.content_widget.setCurrentIndex(3)

    def survey_end_show(self):
        msg_box = QMessageBox()
        msg_box.setText("Результаты вашей анкеты сохранены.")
        msg_box.exec()

    def survey_instruction_show(self):
        msg_box = QMessageBox()
        msg_box.setText("«Безопасное место»")
        msg_box.setInformativeText("Инструкция: ответьте на 10 представленных ниже вопросов, "
                                   "выбрав один наиболее подходящий вариант, и получите в результате "
                                   "персональную карточку сценария релаксации RelaxMe.")
        msg_box.exec()

    def closeEvent(self, event: QCloseEvent) -> None:
        if self.eeg_device_service:
            self.eeg_device_service.exit()
        for window in QApplication.topLevelWidgets():
            window.close()

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


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
