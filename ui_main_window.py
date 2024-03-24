# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
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
"}")
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
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.control_frame = QFrame(self.centralwidget)
        self.control_frame.setObjectName(u"control_frame")
        self.control_frame.setFrameShape(QFrame.StyledPanel)
        self.control_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.control_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.raw_data_btn = QPushButton(self.control_frame)
        self.raw_data_btn.setObjectName(u"raw_data_btn")

        self.verticalLayout.addWidget(self.raw_data_btn)

        self.chart_btn = QPushButton(self.control_frame)
        self.chart_btn.setObjectName(u"chart_btn")

        self.verticalLayout.addWidget(self.chart_btn)

        self.classification_btn = QPushButton(self.control_frame)
        self.classification_btn.setObjectName(u"classification_btn")

        self.verticalLayout.addWidget(self.classification_btn)

        self.about_us_btn = QPushButton(self.control_frame)
        self.about_us_btn.setObjectName(u"about_us_btn")

        self.verticalLayout.addWidget(self.about_us_btn)


        self.horizontalLayout.addWidget(self.control_frame)

        self.view_frame = QFrame(self.centralwidget)
        self.view_frame.setObjectName(u"view_frame")
        self.view_frame.setFrameShape(QFrame.StyledPanel)
        self.view_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.view_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.view_widget = QStackedWidget(self.view_frame)
        self.view_widget.setObjectName(u"view_widget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.raw_data_label = QLabel(self.frame_2)
        self.raw_data_label.setObjectName(u"raw_data_label")
        self.raw_data_label.setScaledContents(False)
        self.raw_data_label.setWordWrap(False)

        self.verticalLayout_4.addWidget(self.raw_data_label, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.raw_data_frame = QFrame(self.page)
        self.raw_data_frame.setObjectName(u"raw_data_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.raw_data_frame.sizePolicy().hasHeightForWidth())
        self.raw_data_frame.setSizePolicy(sizePolicy)
        self.raw_data_frame.setFrameShape(QFrame.StyledPanel)
        self.raw_data_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.raw_data_frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.scrollArea = QScrollArea(self.raw_data_frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 550, 404))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.raw_data_layout = QVBoxLayout()
        self.raw_data_layout.setSpacing(0)
        self.raw_data_layout.setObjectName(u"raw_data_layout")
        self.raw_data_layout.setContentsMargins(-1, 0, -1, -1)

        self.verticalLayout_13.addLayout(self.raw_data_layout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_12.addWidget(self.scrollArea)


        self.verticalLayout_3.addWidget(self.raw_data_frame)

        self.view_widget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_3 = QFrame(self.page_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.chart_label = QLabel(self.frame_3)
        self.chart_label.setObjectName(u"chart_label")
        self.chart_label.setScaledContents(False)
        self.chart_label.setWordWrap(False)

        self.verticalLayout_5.addWidget(self.chart_label, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.chart_frame = QFrame(self.page_2)
        self.chart_frame.setObjectName(u"chart_frame")
        sizePolicy.setHeightForWidth(self.chart_frame.sizePolicy().hasHeightForWidth())
        self.chart_frame.setSizePolicy(sizePolicy)
        self.chart_frame.setFrameShape(QFrame.StyledPanel)
        self.chart_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.chart_frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.chart_layout = QHBoxLayout()
        self.chart_layout.setObjectName(u"chart_layout")

        self.verticalLayout_11.addLayout(self.chart_layout)


        self.verticalLayout_6.addWidget(self.chart_frame)

        self.view_widget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_4 = QFrame(self.page_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.classification_label = QLabel(self.frame_4)
        self.classification_label.setObjectName(u"classification_label")
        self.classification_label.setScaledContents(False)
        self.classification_label.setWordWrap(False)

        self.verticalLayout_7.addWidget(self.classification_label, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.frame_4)

        self.classification_frame = QFrame(self.page_3)
        self.classification_frame.setObjectName(u"classification_frame")
        sizePolicy.setHeightForWidth(self.classification_frame.sizePolicy().hasHeightForWidth())
        self.classification_frame.setSizePolicy(sizePolicy)
        self.classification_frame.setFrameShape(QFrame.StyledPanel)
        self.classification_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.classification_frame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.classification_layout = QVBoxLayout()
        self.classification_layout.setObjectName(u"classification_layout")

        self.verticalLayout_14.addLayout(self.classification_layout)


        self.verticalLayout_8.addWidget(self.classification_frame)

        self.view_widget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_10 = QVBoxLayout(self.page_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_5 = QFrame(self.page_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.about_us_label = QLabel(self.frame_5)
        self.about_us_label.setObjectName(u"about_us_label")
        font = QFont()
        font.setWeight(QFont.ExtraBold)
        self.about_us_label.setFont(font)
        self.about_us_label.setScaledContents(False)
        self.about_us_label.setWordWrap(False)

        self.verticalLayout_9.addWidget(self.about_us_label, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_10.addWidget(self.frame_5)

        self.about_us_frame = QFrame(self.page_4)
        self.about_us_frame.setObjectName(u"about_us_frame")
        sizePolicy.setHeightForWidth(self.about_us_frame.sizePolicy().hasHeightForWidth())
        self.about_us_frame.setSizePolicy(sizePolicy)
        self.about_us_frame.setFrameShape(QFrame.StyledPanel)
        self.about_us_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.about_us_frame)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.about_us_content_label = QLabel(self.about_us_frame)
        self.about_us_content_label.setObjectName(u"about_us_content_label")
        self.about_us_content_label.setEnabled(True)
        self.about_us_content_label.setMinimumSize(QSize(0, 0))
        self.about_us_content_label.setMaximumSize(QSize(1000, 1000))
        self.about_us_content_label.setScaledContents(False)
        self.about_us_content_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.about_us_content_label)


        self.verticalLayout_15.addLayout(self.horizontalLayout_2)


        self.verticalLayout_10.addWidget(self.about_us_frame)

        self.view_widget.addWidget(self.page_4)

        self.verticalLayout_2.addWidget(self.view_widget)


        self.horizontalLayout.addWidget(self.view_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 812, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.open_file_action)
        self.menu_2.addAction(self.light_theme_action)
        self.menu_2.addAction(self.dark_theme_action)

        self.retranslateUi(MainWindow)

        self.view_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u043e\u0442\u0440\u0438\u0442\u0435\u043b\u044c \u042d\u042d\u0413", None))
        self.open_file_action.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b...", None))
        self.light_theme_action.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u0435\u0442\u043b\u0430\u044f", None))
        self.dark_theme_action.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0451\u043c\u043d\u0430\u044f", None))
        self.raw_data_btn.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a \u042d\u042d\u0413", None))
        self.chart_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u044b", None))
        self.classification_btn.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0430\u0441\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f", None))
        self.about_us_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e \u043d\u0430\u0441", None))
        self.raw_data_label.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a \u042d\u042d\u0413", None))
        self.chart_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u044b", None))
        self.classification_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0430\u0441\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u0432\u043e\u043e\u0431\u0440\u0430\u0436\u0430\u0435\u043c\u043e\u0433\u043e \u0434\u0432\u0438\u0436\u0435\u043d\u0438\u044f", None))
        self.about_us_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e \u043d\u0430\u0448\u0443 \u043a\u043e\u043c\u0430\u043d\u0434\u0443", None))
        self.about_us_content_label.setText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u0430", None))
    # retranslateUi

