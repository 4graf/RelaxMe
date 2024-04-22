from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView


class SurveyWindow(QMainWindow):
    def __init__(self, content_url):
        super().__init__()

        self.setWindowTitle('Form')
        self.setGeometry(100, 100, 800, 600)

        self.web_view = QWebEngineView()
        self.web_view.setUrl(content_url)

        layout = QVBoxLayout()
        layout.addWidget(self.web_view)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
