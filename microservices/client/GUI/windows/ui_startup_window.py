# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_startup_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)

class Ui_StartupWindow(object):
    def setupUi(self, StartUpWindow):
        if not StartUpWindow.objectName():
            StartUpWindow.setObjectName(u"StartUpWindow")
        StartUpWindow.resize(812, 583)
        StartUpWindow.setStyleSheet(u"#MainWindow *{\n"
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
        self.open_file_action = QAction(StartUpWindow)
        self.open_file_action.setObjectName(u"open_file_action")
        self.light_theme_action = QAction(StartUpWindow)
        self.light_theme_action.setObjectName(u"light_theme_action")
        self.light_theme_action.setCheckable(True)
        self.light_theme_action.setEnabled(True)
        self.dark_theme_action = QAction(StartUpWindow)
        self.dark_theme_action.setObjectName(u"dark_theme_action")
        self.dark_theme_action.setCheckable(True)
        self.dark_theme_action.setChecked(True)
        self.dark_theme_action.setEnabled(True)
        self.centralwidget = QWidget(StartUpWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.content_widget = QStackedWidget(self.centralwidget)
        self.content_widget.setObjectName(u"content_widget")
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.verticalLayout = QVBoxLayout(self.main_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.stress_video_btn = QPushButton(self.main_page)
        self.stress_video_btn.setObjectName(u"stress_video_btn")

        self.gridLayout.addWidget(self.stress_video_btn, 3, 1, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.testing_btn = QPushButton(self.main_page)
        self.testing_btn.setObjectName(u"testing_btn")

        self.gridLayout.addWidget(self.testing_btn, 3, 0, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.instruction_btn = QPushButton(self.main_page)
        self.instruction_btn.setObjectName(u"instruction_btn")

        self.gridLayout.addWidget(self.instruction_btn, 3, 2, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.start_btn = QPushButton(self.main_page)
        self.start_btn.setObjectName(u"start_btn")

        self.gridLayout.addWidget(self.start_btn, 0, 1, 1, 1, Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addLayout(self.gridLayout)

        self.content_widget.addWidget(self.main_page)
        self.testing_page = QWidget()
        self.testing_page.setObjectName(u"testing_page")
        self.verticalLayout_3 = QVBoxLayout(self.testing_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.question_label = QLabel(self.testing_page)
        self.question_label.setObjectName(u"question_label")

        self.verticalLayout_2.addWidget(self.question_label)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.radioButton = QRadioButton(self.testing_page)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_4.addWidget(self.radioButton)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.pushButton = QPushButton(self.testing_page)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.content_widget.addWidget(self.testing_page)

        self.gridLayout_2.addWidget(self.content_widget, 1, 0, 1, 1)

        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.header_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignLeft)

        self.main_label = QLabel(self.header_frame)
        self.main_label.setObjectName(u"main_label")

        self.horizontalLayout.addWidget(self.main_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.change_theme_btn = QPushButton(self.header_frame)
        self.change_theme_btn.setObjectName(u"change_theme_btn")
        self.change_theme_btn.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.change_theme_btn, 0, Qt.AlignmentFlag.AlignRight)


        self.gridLayout_2.addWidget(self.header_frame, 0, 0, 1, 1)

        StartUpWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartUpWindow)

        QMetaObject.connectSlotsByName(StartUpWindow)
    # setupUi

    def retranslateUi(self, StartUpWindow):
        StartUpWindow.setWindowTitle(QCoreApplication.translate("StartUpWindow", u"MyRelax - Hub", None))
        self.open_file_action.setText(QCoreApplication.translate("StartUpWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b...", None))
        self.light_theme_action.setText(QCoreApplication.translate("StartUpWindow", u"\u0421\u0432\u0435\u0442\u043b\u0430\u044f", None))
        self.dark_theme_action.setText(QCoreApplication.translate("StartUpWindow", u"\u0422\u0451\u043c\u043d\u0430\u044f", None))
        self.stress_video_btn.setText(QCoreApplication.translate("StartUpWindow", u"\u0421\u0442\u0440\u0435\u0441\u0441\u043e\u0432\u043e\u0435 \u0432\u0438\u0434\u0435\u043e", None))
        self.testing_btn.setText(QCoreApplication.translate("StartUpWindow", u"\u041f\u0440\u043e\u0439\u0442\u0438 \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.instruction_btn.setText(QCoreApplication.translate("StartUpWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f", None))
        self.start_btn.setText(QCoreApplication.translate("StartUpWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0440\u0435\u043b\u0430\u043a\u0441", None))
        self.question_label.setText(QCoreApplication.translate("StartUpWindow", u"question", None))
        self.radioButton.setText(QCoreApplication.translate("StartUpWindow", u"RadioButton", None))
        self.pushButton.setText(QCoreApplication.translate("StartUpWindow", u"\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u044c", None))
        self.label_2.setText("")
        self.main_label.setText(QCoreApplication.translate("StartUpWindow", u"MyRelax", None))
        self.change_theme_btn.setText(QCoreApplication.translate("StartUpWindow", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u0442\u0435\u043c\u0443", None))
    # retranslateUi

