# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_relax_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_RelaxWindow(object):
    def setupUi(self, RelaxWindow):
        if not RelaxWindow.objectName():
            RelaxWindow.setObjectName(u"RelaxWindow")
        RelaxWindow.resize(812, 583)
        RelaxWindow.setStyleSheet(u"#MainWindow *{\n"
"  background-color: #f0f3ff;\n"
"}\n"
"\n"
"#centralwidget QLabel{\n"
"  color: #000000;\n"
"  font-size: 24px;\n"
"  font-weight: 800;\n"
"}\n"
"\n"
"QPushButton{\n"
"  padding: 12px 24px;\n"
"  border-style: inset;\n"
"  border-width: 3px;\n"
"  border-radius: 20px;\n"
"  border-color: #816e9c;\n"
"  background: #f5f6fc;\n"
"  color: #000000;\n"
"  font-size: 14px;\n"
"  font-weight: 600;\n"
"  margin: 20px 0px;\n"
"}\n"
"\n"
"")
        self.open_file_action = QAction(RelaxWindow)
        self.open_file_action.setObjectName(u"open_file_action")
        self.light_theme_action = QAction(RelaxWindow)
        self.light_theme_action.setObjectName(u"light_theme_action")
        self.light_theme_action.setCheckable(True)
        self.light_theme_action.setEnabled(True)
        self.dark_theme_action = QAction(RelaxWindow)
        self.dark_theme_action.setObjectName(u"dark_theme_action")
        self.dark_theme_action.setCheckable(True)
        self.dark_theme_action.setChecked(True)
        self.dark_theme_action.setEnabled(True)
        self.centralwidget = QWidget(RelaxWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.content_widget = QStackedWidget(self.centralwidget)
        self.content_widget.setObjectName(u"content_widget")
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.verticalLayout = QVBoxLayout(self.main_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.main_page)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(448, 32))
        self.label.setMaximumSize(QSize(16777215, 32))

        self.verticalLayout_5.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.video_grid_layout = QGridLayout()
        self.video_grid_layout.setObjectName(u"video_grid_layout")

        self.verticalLayout_5.addLayout(self.video_grid_layout)


        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.content_widget.addWidget(self.main_page)
        self.player_page = QWidget()
        self.player_page.setObjectName(u"player_page")
        self.verticalLayout_3 = QVBoxLayout(self.player_page)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.player_video_layout = QHBoxLayout()
        self.player_video_layout.setObjectName(u"player_video_layout")

        self.verticalLayout_3.addLayout(self.player_video_layout)

        self.player_panel = QHBoxLayout()
        self.player_panel.setObjectName(u"player_panel")
        self.back_button = QPushButton(self.player_page)
        self.back_button.setObjectName(u"back_button")

        self.player_panel.addWidget(self.back_button, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_3.addLayout(self.player_panel)

        self.verticalLayout_3.setStretch(0, 10)
        self.content_widget.addWidget(self.player_page)

        self.gridLayout_2.addWidget(self.content_widget, 0, 0, 1, 1)

        RelaxWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RelaxWindow)

        self.content_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(RelaxWindow)
    # setupUi

    def retranslateUi(self, RelaxWindow):
        RelaxWindow.setWindowTitle(QCoreApplication.translate("RelaxWindow", u"RelaxMe - Relax", None))
        self.open_file_action.setText(QCoreApplication.translate("RelaxWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b...", None))
        self.light_theme_action.setText(QCoreApplication.translate("RelaxWindow", u"\u0421\u0432\u0435\u0442\u043b\u0430\u044f", None))
        self.dark_theme_action.setText(QCoreApplication.translate("RelaxWindow", u"\u0422\u0451\u043c\u043d\u0430\u044f", None))
        self.label.setText(QCoreApplication.translate("RelaxWindow", u"\u0412\u042b\u0411\u0415\u0420\u0418\u0422\u0415 \u0412\u0418\u0414\u0415\u041e \u0414\u041b\u042f \u0420\u0415\u041b\u0410\u041a\u0421\u0410\u0426\u0418\u0418", None))
        self.back_button.setText(QCoreApplication.translate("RelaxWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

