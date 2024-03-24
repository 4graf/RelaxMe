from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView


class VideoWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('YouTube Video Player')
        self.setGeometry(100, 100, 800, 600)

        video_id = "eRQklf9vxBQ"
        video_url = (f"https://www.youtube.com/embed/{video_id}?autoplay=1&controls=1&"
                     f"modestbranding=1&showinfo=0&fs=0&rel=0&color=white")

        self.web_view = QWebEngineView()
        self.web_view.setUrl(video_url)

        layout = QVBoxLayout()
        layout.addWidget(self.web_view)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
