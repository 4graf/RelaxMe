# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_startupwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_StartupWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(812, 583)
        MainWindow.setStyleSheet(u"#MainWindow *{\n"
"  background-color: #202020;\n"
"}\n"
"\n"
"#menubar {\n"
"  background-color: #2b2b2b;\n"
"  color: #FFFFFF;\n"
"}\n"
"\n"
"QMenu {\n"
"  background-color: #2b2b2b;\n"
"  color: #FFFFFF;\n"
"}\n"
"\n"
"#centralwidget QLabel{\n"
"  color: #FFFFFF;\n"
"  font-size: 24px;\n"
"  font-weight: 800;\n"
"}\n"
"\n"
"#control_frame QPushButton{\n"
"  padding: 12px 24px;\n"
"  border-style: inset;\n"
"  border-width: 3px;\n"
"  border-radius: 20px;\n"
"  border-color: #63C700;\n"
"  background: none;\n"
"  color: #FFFFFF;\n"
"  font-size: 14px;\n"
"  font-weight: 600;\n"
"  margin: 20px 0px;\n"
"}\n"
"\n"
"QPushButton{\n"
"  padding: 12px 24px;\n"
"  border-style: inset;\n"
"  border-width: 3px;\n"
"  border-radius: 20px;\n"
"  border-color: #63C700;\n"
"  background: none;\n"
"  color: #FFFFFF;\n"
"  font-size: 14px;\n"
"  font-weight: 600;\n"
"}\n"
"\n"
"")
        self.open_file_action = QAction(MainWindow)
        self.open_file_action.setObjectName(u"open_file_action")
        self.light_theme_action = QAction(MainWindow)
        self.light_theme_action.setObjectName(u"light_theme_action")
        self.light_theme_action.setCheckable(True)
        self.light_theme_action.setEnabled(True)
        self.dark_theme_action = QAction(MainWindow)
        self.dark_theme_action.setObjectName(u"dark_theme_action")
        self.dark_theme_action.setCheckable(True)
        self.dark_theme_action.setChecked(True)
        self.dark_theme_action.setEnabled(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.stress_video_btn = QPushButton(self.page)
        self.stress_video_btn.setObjectName(u"stress_video_btn")

        self.gridLayout.addWidget(self.stress_video_btn, 3, 1, 1, 1)

        self.testing_btn = QPushButton(self.page)
        self.testing_btn.setObjectName(u"testing_btn")

        self.gridLayout.addWidget(self.testing_btn, 3, 0, 1, 1)

        self.instruction_btn = QPushButton(self.page)
        self.instruction_btn.setObjectName(u"instruction_btn")

        self.gridLayout.addWidget(self.instruction_btn, 3, 2, 1, 1)

        self.start_btn = QPushButton(self.page)
        self.start_btn.setObjectName(u"start_btn")

        self.gridLayout.addWidget(self.start_btn, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_2.addWidget(self.stackedWidget, 1, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2, 0, Qt.AlignLeft)

        self.main_label = QLabel(self.frame)
        self.main_label.setObjectName(u"main_label")

        self.horizontalLayout.addWidget(self.main_label, 0, Qt.AlignHCenter)

        self.change_theme_btn = QPushButton(self.frame)
        self.change_theme_btn.setObjectName(u"change_theme_btn")
        self.change_theme_btn.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.change_theme_btn, 0, Qt.AlignRight)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MyRelax - Hub", None))
        self.open_file_action.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b...", None))
        self.light_theme_action.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u0435\u0442\u043b\u0430\u044f", None))
        self.dark_theme_action.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0451\u043c\u043d\u0430\u044f", None))
        self.stress_video_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0435\u0441\u0441\u043e\u0432\u043e\u0435 \u0432\u0438\u0434\u0435\u043e", None))
        self.testing_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0439\u0442\u0438 \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.instruction_btn.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f", None))
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0440\u0435\u043b\u0430\u043a\u0441", None))
        self.label_2.setText("")
        self.main_label.setText(QCoreApplication.translate("MainWindow", u"MyRelax", None))
        self.change_theme_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u0442\u0435\u043c\u0443", None))
    # retranslateUi

