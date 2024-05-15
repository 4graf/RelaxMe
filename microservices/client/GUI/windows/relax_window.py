# import matplotlib
# import matplotlib.pyplot as plt
# import mne
# import numpy as np
from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow, QWidget, QTableView, QTableWidget, QVBoxLayout, QPushButton

from microservices.client.GUI.windows.ui_relax_window import Ui_RelaxWindow
from microservices.client.GUI.windows.video_window import get_video_widget


# from matplotlib.backends.backend_qtagg import (FigureCanvasQTAgg as FigureCanvas,
#                                                NavigationToolbar2QT as NavigationToolbar)

# from classification import EEGClassifier
# from preprocessing import EEGPreprocessing


# matplotlib.use('Qt5Agg')
# mne.viz.set_browser_backend('qt')


class PlotWidget(QWidget):
    def __init__(self, figure, parent=None):
        super(PlotWidget, self).__init__(parent)
        # self.canvas = FigureCanvas(figure)
        # self.canvas.draw()
        # self.canvas.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus | QtCore.Qt.FocusPolicy.WheelFocus)
        # self.canvas.setFocus()


class RelaxWindow(QMainWindow):
    def __init__(self, video_urls):
        super(RelaxWindow, self).__init__()
        self.ui = Ui_RelaxWindow()
        self.ui.setupUi(self)

        self._size_grid = (3, 3)
        self.video_btns = {}
        self.video_urls = video_urls

        self.all_video_show()

        self.ui.back_button.clicked.connect(self.back_to_menu)
        # self.ui.chart_btn.clicked.connect(self.chart_show)
        # self.ui.classification_btn.clicked.connect(self.classification_show)
        # self.ui.about_us_btn.clicked.connect(self.about_us_show)
        # self.ui.open_file_action.triggered.connect(self.open_file)
        # self.ui.light_theme_action.triggered.connect(self.make_light_theme)
        # self.ui.dark_theme_action.triggered.connect(self.make_dark_theme)

        # self.record_idx = self.eeg_preproc.filenames.index('data/Артемий правая нога.txt')

        # self._draw_about_us()

        self.showMaximized()

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

    def back_to_menu(self):
        self._clear_children(self.ui.player_video_layout)
        self.all_video_show()

    def chart_show(self):
        self.ui.view_widget.setCurrentIndex(1)

    def classification_show(self):
        self.ui.view_widget.setCurrentIndex(2)

    def about_us_show(self):
        self.ui.view_widget.setCurrentIndex(3)

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
