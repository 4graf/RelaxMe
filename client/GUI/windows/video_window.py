from PySide6.QtWebEngineCore import QWebEngineSettings
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton
from PySide6.QtWebEngineWidgets import QWebEngineView


class VideoWindow(QMainWindow):
    def __init__(self, video_id):
        super().__init__()

        self.setWindowTitle('YouTube Video Player')
        self.setGeometry(100, 100, 800, 600)

        video_url = (f"https://www.youtube.com/embed/{video_id}?autoplay=1&controls=1&"
                     f"modestbranding=1&showinfo=0&fs=0&rel=0&color=white")

        self.web_view = QWebEngineView()
        self.web_view.setUrl(video_url)

        layout = QVBoxLayout()
        layout.addWidget(self.web_view)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


class VideoWidget(QWidget):
    def __init__(self, video_id):
        super(VideoWidget, self).__init__()

        # self.setWindowTitle('YouTube Video Player')
        self.setGeometry(100, 100, 800, 600)

        video_url = (f"https://www.youtube.com/embed/{video_id}?autoplay=1&controls=1&"
                     f"modestbranding=1&showinfo=0&fs=0&rel=0&color=white")

        self.web_view = QWebEngineView()
        self.web_view.setUrl(video_url)

        layout = QVBoxLayout()
        layout.addWidget(self.web_view)

        self.setLayout(layout)

class TestWidget(QPushButton):
    def __init__(self, video_id):
        super(TestWidget, self).__init__()

        # self.setWindowTitle('YouTube Video Player')
        self.setGeometry(100, 100, 800, 600)

        self.web_view = get_video_widget(video_id)

        layout = QVBoxLayout()
        layout.addWidget(self.web_view)

        self.setLayout(layout)


def get_video_widget(video_id, autoplay=False, start=0, mute=False):
    if autoplay:
        autoplay_param = 1
    else:
        autoplay_param = 0

    if mute:
        mute_param = 1
    else:
        mute_param = 0

    video_url = (f"https://www.youtube.com/embed/{video_id}?autoplay={autoplay_param}&controls=1&"
                 f"modestbranding=1&showinfo=0&fs=1&rel=0&color=white&start={start}&mute={mute_param}")

    web_view = QWebEngineView()
    web_view.setUrl(video_url)
    web_view.page().settings().setAttribute(QWebEngineSettings.WebAttribute.PlaybackRequiresUserGesture, False)
    web_view.settings().setAttribute(QWebEngineSettings.WebAttribute.FullScreenSupportEnabled, True)
    web_view.page().fullScreenRequested.connect(lambda request: request.accept())

    return web_view
