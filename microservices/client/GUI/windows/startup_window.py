import sys

from PySide6.QtCore import QUrl, QFileInfo
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QApplication, QRadioButton, QButtonGroup, QMessageBox
from PySide6.QtWidgets import QMainWindow, QWidget

from microservices.client.GUI.settings import stress_video_id
from microservices.client.GUI.utils import QUESTIONARY
from microservices.client.GUI.windows.relax_window import RelaxWindow
from microservices.client.GUI.windows.themes import ThemeGUI
from microservices.client.GUI.windows.ui_startup_window import Ui_StartupWindow
from microservices.client.GUI.windows.video_window import VideoWindow, get_video_widget, TestWidget
from microservices.client.safe_place.safe_place import SafePlaceDecider


class PlotWidget(QWidget):
    def __init__(self, parent=None):
        super(PlotWidget, self).__init__(parent)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_StartupWindow()
        self.ui.setupUi(self)

        self.stress_video_window = None
        self.relax_window = None
        self.survey_window = None
        self.player = None

        self.questionary = QUESTIONARY
        self.questionary_results = None
        self.questionary_current_id = -1
        self.quest_button_group = None

        self.ui.start_btn.clicked.connect(self.start_relax)
        self.ui.stress_video_btn.clicked.connect(self.open_stress_video)
        self.ui.testing_btn.clicked.connect(self.survey_show)
        self.ui.pushButton.clicked.connect(self.survey_next)

        self.showMaximized()

        # self.ui.gridLayout.addWidget(TestWidget(stress_video_id))

    def start_relax(self):
        if not self.relax_window or not self.relax_window.isVisible():
            self.relax_window = RelaxWindow([stress_video_id] * 6)
            self.relax_window.show()

    def open_stress_video(self):
        if not self.stress_video_window or not self.stress_video_window.isVisible():
            self.player = QMediaPlayer()
            # self.player.setSource(QUrl.fromLocalFile(QFileInfo('microservices/client/video/Stress video.mp4').absoluteFilePath()))
            self.player.setSource(QUrl.fromLocalFile(QFileInfo('../video/Stress video.mp4').absoluteFilePath()))
            self.stress_video_window = QVideoWidget()
            self.audio_output = QAudioOutput()
            self.player.setAudioOutput(self.audio_output)
            self.player.setVideoOutput(self.stress_video_window)
            self.stress_video_window.show()
            self.player.play()
        # if not self.stress_video_window or not self.stress_video_window.isVisible():
        #     self.stress_video_window = VideoWindow(stress_video_id)
        #     self.stress_video_window.show()

    def survey_next(self):
        # if not self.survey_window or not self.survey_window.isVisible():
        #     self.survey_window = SurveyWindow(survey_url)
        #     self.survey_window.show()

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
            print(SafePlaceDecider.all_places[tuple(res.items())])

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

    def startup_show(self) -> None:
        self.ui.content_widget.setCurrentIndex(0)

    def survey_show(self):
        self.questionary_results = []

        self.survey_instruction_show()

        self.survey_next()
        self.ui.content_widget.setCurrentIndex(1)

    def result_show(self):
        ...
        self.ui.content_widget.setCurrentIndex(2)

    def survey_end_show(self):
        msg_box = QMessageBox()
        msg_box.setText("Результаты вашей анкеты сохранены.")
        # msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        # msgBox.setDefaultButton(QMessageBox.Save)
        msg_box.exec()

    def survey_instruction_show(self):
        msg_box = QMessageBox()
        msg_box.setText("«Безопасное место»")
        msg_box.setInformativeText("Инструкция: ответьте на 10 представленных ниже вопросов, "
                                   "выбрав один наиболее подходящий вариант, и получите в результате "
                                   "персональную карточку сценария релаксации RelaxMe.")
        # msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        # msgBox.setDefaultButton(QMessageBox.Save)
        msg_box.exec()

    # def classification_show(self):
    #     self.ui.view_widget.setCurrentIndex(2)
    #
    # def about_us_show(self):
    #     self.ui.view_widget.setCurrentIndex(3)

    @staticmethod
    def _clear_children(parent):
        while parent.count():
            child = parent.takeAt(0)
            child_widget = child.widget()
            if child_widget:
                child_widget.setParent(None)
                child_widget.deleteLater()

    # def _draw_raw_data(self):
    #     self._clear_children(self.ui.raw_data_layout)
    #
    #     real_raw = self.eeg_preproc.filt_raw[self.record_idx][0]
    #     real_raw.pick('eeg', exclude=['event'])
    #     imagine_raw = self.eeg_preproc.filt_raw[self.record_idx][1]
    #     imagine_raw.pick('eeg', exclude=['event'])
    #
    #     fig1 = real_raw.plot(block=False, scalings='auto', show=False);
    #     fig1.setMinimumHeight(400)
    #     self.ui.raw_data_layout.addWidget(fig1)
    #
    #     fig2 = imagine_raw.plot(block=False, scalings='auto', show=False);
    #     fig2.setMinimumHeight(400)
    #     self.ui.raw_data_layout.addWidget(fig2)
    #
    #     psd_real = real_raw.compute_psd()
    #     fig3 = psd_real.plot(show=False);
    #     canvas_real = PlotWidget(fig3).canvas
    #     canvas_real.setMinimumHeight(400)
    #     self.ui.raw_data_layout.addWidget(canvas_real)
    #
    #     psd_imagine = imagine_raw.compute_psd()
    #     fig4 = psd_imagine.plot(show=False);
    #     canvas_imagine = PlotWidget(fig4).canvas
    #     canvas_imagine.setMinimumHeight(400)
    #     self.ui.raw_data_layout.addWidget(canvas_imagine)
    #
    # def _draw_chart(self):
    #     self._clear_children(self.ui.chart_layout)
    #
    #     test_df = self.ans[self.ans['name'] == self.record_idx]
    #     test_df.index = np.arange(len(test_df))
    #     fig, axs = plt.subplots(2)
    #
    #     self.eeg_preproc.create_hist(self.ans, test_df, 'Fp1', 'max', axs[0])
    #     self.eeg_preproc.create_fourier(self.ans, test_df, 'Fp1', 50, axs[1])
    #
    #     canvas = PlotWidget(fig).canvas
    #     self.ui.chart_layout.addWidget(NavigationToolbar(canvas))
    #     self.ui.chart_layout.addWidget(canvas)
    #
    # def _draw_classification(self):
    #     self._clear_children(self.ui.classification_layout)
    #
    #     ans_name = self.ans[self.ans['name'] == self.record_idx]
    #     X, y = self.eeg_class.load_data(df=ans_name)
    #     X_test = self.eeg_class.preprocess_data(X)
    #     pred_real = self.eeg_class.predict_eeg(X_test, 'real')
    #     pred_body = self.eeg_class.predict_eeg(X_test, 'body_part')
    #     pred_action = self.eeg_class.predict_eeg(X_test, 'action')
    #
    #     filt_raw_real = self.eeg_preproc.filt_raw[self.record_idx][0].copy()
    #     filt_raw_imagine = self.eeg_preproc.filt_raw[self.record_idx][1].copy()
    #     data_real, times_real = filt_raw_real.get_data(return_times=True)
    #     data_imagine, times_imagine = filt_raw_imagine.get_data(return_times=True)
    #
    #     cls_event_idx = 0
    #     start = 0
    #     onsets = []
    #     durations = []
    #     descriptions = []
    #     last_event = None
    #     for i, event in enumerate(data_real[-1]):
    #         if not np.isnan(event):
    #             if event == last_event:
    #                 onsets.append(start)
    #                 durations.append(times_real[i]-start)
    #                 real = 'real' if pred_real[cls_event_idx] == 1 else 'imagine'
    #                 body = 'arm' if pred_body[cls_event_idx] == 1 else 'leg'
    #                 action = 'pos' if pred_action[cls_event_idx] == 1 else 'neg'
    #                 descriptions.append(f'{real}_{body}_{action}')
    #                 cls_event_idx += 1
    #             else:
    #                 last_event = event
    #                 start = times_real[i]
    #
    #     annotations_real = mne.Annotations(onsets, durations, descriptions)
    #     filt_raw_real.set_annotations(annotations_real)
    #
    #     start = 0
    #     onsets = []
    #     durations = []
    #     descriptions = []
    #     last_event = None
    #     for i, event in enumerate(data_imagine[-1]):
    #         if not np.isnan(event):
    #             if event == last_event:
    #                 onsets.append(start)
    #                 durations.append(times_imagine[i]-start)
    #                 real = 'real' if pred_real[cls_event_idx] == 1 else 'imagine'
    #                 body = 'arm' if pred_body[cls_event_idx] == 1 else 'leg'
    #                 action = 'pos' if pred_action[cls_event_idx] == 1 else 'neg'
    #                 descriptions.append(f'{real}_{body}_{action}')
    #                 cls_event_idx += 1
    #             else:
    #                 last_event = event
    #                 start = times_imagine[i]
    #
    #     annotations_imagine = mne.Annotations(onsets, durations, descriptions)
    #     filt_raw_imagine.set_annotations(annotations_imagine)
    #
    #     fig1 = filt_raw_real.pick('eeg', exclude=['event']).plot(block=False, scalings='auto', show=False);
    #     fig1.setMinimumHeight(400)
    #     self.ui.classification_layout.addWidget(fig1)
    #
    #     fig2 = filt_raw_imagine.pick('eeg', exclude=['event']).plot(block=False, scalings='auto', show=False);
    #     fig2.setMinimumHeight(400)
    #     self.ui.classification_layout.addWidget(fig2)
    #
    # def _draw_about_us(self):
    #     pixmap = QPixmap('resources/about_us_middle.jpg')
    #     self.ui.about_us_content_label.setPixmap(pixmap)
    #     self.ui.about_us_content_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
