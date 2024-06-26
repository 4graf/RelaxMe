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
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QStackedWidget, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_StartupWindow(object):
    def setupUi(self, StartupWindow):
        if not StartupWindow.objectName():
            StartupWindow.setObjectName(u"StartupWindow")
        StartupWindow.resize(812, 583)
        StartupWindow.setStyleSheet(u"* {\n"
"  font-family: 'Circe Rounded';\n"
"  color: #444444;\n"
"  box-sizing: border-box;\n"
"}\n"
"\n"
"QWidget {\n"
"  width: 100%;\n"
"  display: flex;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"\n"
"  background-color: #F0F2FF;\n"
"}\n"
"\n"
"QPushButton {\n"
"  padding: 14px 24px;\n"
"  border-style: solid;\n"
"  border-width: 3px;\n"
"  border-radius: 25px;\n"
"  border-color: #C0AEE2;\n"
"  background: white;\n"
"  color: black;\n"
"  font-size: 18px;\n"
"  font-weight: 400;\n"
"  margin: 15;\n"
"}\n"
"\n"
"#start_btn {\n"
"  font-family: 'Circe Rounded Alt';\n"
"  padding: 18px 36px;\n"
"  border-radius: 36px;\n"
"  background: #8D74BC;\n"
"  color: #FFFFFF;\n"
"  font-size: 24px;\n"
"  font-weight: 800;\n"
"  margin: 0px 0px;\n"
"}\n"
"\n"
"#instruction_back_btn{\n"
"  margin: 0px 0px;\n"
"\n"
"}\n"
"\n"
"QLabel {\n"
"  font-family: 'Circe';\n"
"  margin-top: 0px;\n"
"  font-size: 24px;\n"
"  font-weight: 800;\n"
"  margin-bottom: 0px;\n"
"  text-align: center;\n"
"\n"
"  backgrou"
                        "nd: white;\n"
"}\n"
"\n"
"#auth_label {\n"
"  background: None;\n"
"}\n"
"\n"
"#header_frame {\n"
"  margin-top: -100px;\n"
"  border-radius: 100%;\n"
"  background: white;\n"
"  margin-right: -20;\n"
"  margin-left: -20;\n"
"  margin-bottom: 20px;\n"
"}\n"
"\n"
"#question_label {\n"
"  padding: 15;\n"
"}\n"
"\n"
"QTextBrowser {\n"
"  border: None;\n"
"}\n"
"\n"
"QRadioButton {\n"
"  color: black;\n"
"  font-size: 18px;\n"
"  font-weight: 400;\n"
"}")
        self.open_file_action = QAction(StartupWindow)
        self.open_file_action.setObjectName(u"open_file_action")
        self.light_theme_action = QAction(StartupWindow)
        self.light_theme_action.setObjectName(u"light_theme_action")
        self.light_theme_action.setCheckable(True)
        self.light_theme_action.setEnabled(True)
        self.dark_theme_action = QAction(StartupWindow)
        self.dark_theme_action.setObjectName(u"dark_theme_action")
        self.dark_theme_action.setCheckable(True)
        self.dark_theme_action.setChecked(True)
        self.dark_theme_action.setEnabled(True)
        self.centralwidget = QWidget(StartupWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMinimumSize(QSize(0, 0))
        self.header_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.header_frame.setLineWidth(0)
        self.header_frame.setMidLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.main_label = QLabel(self.header_frame)
        self.main_label.setObjectName(u"main_label")
        self.main_label.setMinimumSize(QSize(140, 85))
        self.main_label.setMaximumSize(QSize(140, 85))
        self.main_label.setPixmap(QPixmap(u"logo.png"))
        self.main_label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.main_label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_5.addWidget(self.header_frame)

        self.content_widget = QStackedWidget(self.centralwidget)
        self.content_widget.setObjectName(u"content_widget")
        self.auth_page = QWidget()
        self.auth_page.setObjectName(u"auth_page")
        self.lineEdit_2 = QLineEdit(self.auth_page)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(240, 160, 331, 41))
        font = QFont()
        font.setFamilies([u"Circe Rounded"])
        font.setPointSize(24)
        self.lineEdit_2.setFont(font)
        self.lineEdit = QLineEdit(self.auth_page)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(240, 230, 331, 41))
        self.lineEdit.setFont(font)
        self.pushButton_2 = QPushButton(self.auth_page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(310, 340, 184, 87))
        self.auth_label = QLabel(self.auth_page)
        self.auth_label.setObjectName(u"auth_label")
        self.auth_label.setGeometry(QRect(180, 40, 441, 29))
        self.auth_label.setAutoFillBackground(False)
        self.auth_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.content_widget.addWidget(self.auth_page)
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
        self.verticalLayout_4.setContentsMargins(15, -1, -1, -1)
        self.radioButton = QRadioButton(self.testing_page)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_4.addWidget(self.radioButton)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.pushButton = QPushButton(self.testing_page)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 3)
        self.verticalLayout_2.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.content_widget.addWidget(self.testing_page)
        self.instruction_page = QWidget()
        self.instruction_page.setObjectName(u"instruction_page")
        self.verticalLayout_6 = QVBoxLayout(self.instruction_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.textBrowser = QTextBrowser(self.instruction_page)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_6.addWidget(self.textBrowser)

        self.instruction_back_btn = QPushButton(self.instruction_page)
        self.instruction_back_btn.setObjectName(u"instruction_back_btn")

        self.verticalLayout_6.addWidget(self.instruction_back_btn, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_6.setStretch(0, 10)
        self.verticalLayout_6.setStretch(1, 1)
        self.content_widget.addWidget(self.instruction_page)

        self.verticalLayout_5.addWidget(self.content_widget)

        self.verticalLayout_5.setStretch(0, 5)
        self.verticalLayout_5.setStretch(1, 19)
        StartupWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartupWindow)

        self.content_widget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(StartupWindow)
    # setupUi

    def retranslateUi(self, StartupWindow):
        StartupWindow.setWindowTitle(QCoreApplication.translate("StartupWindow", u"RelaxMe - Hub", None))
        self.open_file_action.setText(QCoreApplication.translate("StartupWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b...", None))
        self.light_theme_action.setText(QCoreApplication.translate("StartupWindow", u"\u0421\u0432\u0435\u0442\u043b\u0430\u044f", None))
        self.dark_theme_action.setText(QCoreApplication.translate("StartupWindow", u"\u0422\u0451\u043c\u043d\u0430\u044f", None))
        self.main_label.setText("")
        self.lineEdit_2.setText(QCoreApplication.translate("StartupWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.lineEdit.setText(QCoreApplication.translate("StartupWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("StartupWindow", u"\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u044c", None))
        self.auth_label.setText(QCoreApplication.translate("StartupWindow", u"\u0410\u0443\u0442\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f", None))
        self.stress_video_btn.setText(QCoreApplication.translate("StartupWindow", u"\u0421\u0442\u0440\u0435\u0441\u0441\u043e\u0432\u043e\u0435 \u0432\u0438\u0434\u0435\u043e", None))
        self.testing_btn.setText(QCoreApplication.translate("StartupWindow", u"\u041f\u0440\u043e\u0439\u0442\u0438 \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.instruction_btn.setText(QCoreApplication.translate("StartupWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f", None))
        self.start_btn.setText(QCoreApplication.translate("StartupWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0440\u0435\u043b\u0430\u043a\u0441", None))
        self.question_label.setText(QCoreApplication.translate("StartupWindow", u"question", None))
        self.radioButton.setText(QCoreApplication.translate("StartupWindow", u"RadioButton", None))
        self.pushButton.setText(QCoreApplication.translate("StartupWindow", u"\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u044c", None))
        self.textBrowser.setHtml(QCoreApplication.translate("StartupWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Circe Rounded'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700;\">RelaxMe \u2013 \u044d\u0442\u043e \u0441\u0438\u0441\u0442\u0435\u043c\u0430 \u0434\u043b\u044f \u0441\u043d\u0438\u0436\u0435\u043d\u0438\u044f \u0443\u0440\u043e\u0432\u043d\u044f \u0441\u0442\u0440\u0435\u0441\u0441\u0430 \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0430 \u0432\u0438\u0434\u0435"
                        "\u043e\u0437\u0430\u043f\u0438\u0441\u0435\u0439, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0443\u0447\u0438\u0442\u044b\u0432\u0430\u044e\u0442 \u0432\u0430\u0448\u0438 \u043f\u0440\u0435\u0434\u043f\u043e\u0447\u0442\u0435\u043d\u0438\u044f. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:700;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u0412\u044b \u043c\u043e\u0436\u0435\u0442\u0435 \u0441\u043b\u0435\u0434\u0438\u0442\u044c \u0437\u0430 \u043d\u0430\u043b\u0438\u0447\u0438\u0435\u043c \u0443 \u0441\u0435\u0431\u044f \u0441\u0442\u0440\u0435\u0441\u0441\u0430: \u0434\u043b\u044f \u044d\u0442\u043e\u0433\u043e \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u0435 \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u0435 "
                        "\u0434\u043b\u044f \u0437\u0430\u043f\u0438\u0441\u0438 \u042d\u042d\u0413.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:700;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u043c\u044b\u0439 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u044f:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    </span><span style=\" font-size:12pt; font-style:italic;\">1) \u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u042d\u042d\u0413 \u043d\u0435\u0439\u0440\u043e\u0438\u043d\u0442\u0435\u0440\u0444"
                        "\u0435\u0439\u0441 \u0438 \u043d\u0430\u0434\u0435\u0442\u044c \u0435\u0433\u043e \u043d\u0430 \u0441\u0435\u0431\u044f.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">    2) \u041d\u0430\u0436\u0430\u0442\u044c \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 &quot;\u041f\u0440\u043e\u0439\u0442\u0438 \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435&quot; , \u0447\u0442\u043e\u0431\u044b \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c \u0441\u0432\u043e\u0451 \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0435 \u043c\u0435\u0441\u0442\u043e \u0438 \u0442\u0438\u043f \u043b\u0438\u0447\u043d\u043e\u0441\u0442\u0438.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">    3) \u041d\u0430\u0436"
                        "\u0430\u0442\u044c \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 &quot;\u041d\u0430\u0447\u0430\u0442\u044c \u0440\u0435\u043b\u0430\u043a\u0441&quot; \u0438 \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0432 \u043e\u0442\u043a\u0440\u044b\u0432\u0448\u0435\u043c\u0441\u044f \u043e\u043a\u043d\u0435 \u043d\u0430\u0438\u0431\u043e\u043b\u0435\u0435 \u043f\u043e\u043d\u0440\u0430\u0432\u0438\u0432\u0448\u0435\u0435\u0441\u044f \u0432\u0430\u043c \u0432\u0438\u0434\u0435\u043e.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">    4) \u0421\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0432\u0438\u0434\u0435\u043e \u0438 \u0440\u0430\u0441\u0441\u043b\u0430\u0431\u043b\u044f\u0442\u044c\u0441\u044f! </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-"
                        "weight:700;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u0422\u0430\u043a\u0436\u0435 \u0432\u044b \u043c\u043e\u0436\u0435\u0442\u0435 \u043f\u043e\u0443\u0447\u0430\u0441\u0442\u0432\u043e\u0432\u0430\u0442\u044c \u0432 \u0443\u043b\u0443\u0447\u0448\u0435\u043d\u0438\u0438 \u0441\u0438\u0441\u0442\u0435\u043c\u044b RelaxMe, \u0435\u0441\u043b\u0438 \u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0438\u0442\u0435 \u0441\u0442\u0440\u0435\u0441\u0441-\u0432\u0438\u0434\u0435\u043e \u0432 \u043d\u0435\u0439\u0440\u043e\u0438\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441\u0435 \u042d\u042d\u0413. \u042d\u0442\u043e \u043f\u043e\u0437\u0432\u043e\u043b\u0438\u0442 \u0441\u043e\u0431\u0440\u0430\u0442\u044c \u0431\u043e\u043b\u044c\u0448\u0435 \u0434\u0430\u043d\u043d\u044b\u0445 \u0434\u043b\u044f \u0443\u043b\u0443\u0447\u0448\u0435\u043d\u0438\u044f \u043c\u043e\u0434\u0435\u043b\u0435"
                        "\u0439 \u043f\u0440\u0435\u0434\u0441\u043a\u0430\u0437\u0430\u043d\u0438\u044f.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:700;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:700;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-style:italic;\">RelaxMe, \u0438\u0434\u0435\u0439\u043d\u044b\u0439 \u0441\u043e\u0437\u0434\u0430\u0442\u0435\u043b\u044c \u0438 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a \u2013 \u041d"
                        "\u0430\u0431\u0430\u0442\u043e\u0432 \u0410\u0440\u0441\u0435\u043d\u0438\u0439 \u0412\u0430\u0434\u0438\u043c\u043e\u0432\u0438\u0447  </span></p></body></html>", None))
        self.instruction_back_btn.setText(QCoreApplication.translate("StartupWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

