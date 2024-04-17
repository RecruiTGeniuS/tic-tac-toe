# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set_name_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_SetNameWindow(object):
    def setupUi(self, SetNameWindow):
        if not SetNameWindow.objectName():
            SetNameWindow.setObjectName(u"SetNameWindow")
        SetNameWindow.resize(500, 640)
        self.centralwidget = QWidget(SetNameWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 80, 49, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 60, 171, 61))
        font = QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(180, 440, 141, 51))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 200, 61, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(350, 200, 61, 31))
        self.label_4.setFont(font1)
        self.lineX = QLineEdit(self.centralwidget)
        self.lineX.setObjectName(u"lineX")
        self.lineX.setGeometry(QRect(30, 240, 181, 41))
        self.lineX.setMaxLength(30)
        self.lineX.setAlignment(Qt.AlignCenter)
        self.line0 = QLineEdit(self.centralwidget)
        self.line0.setObjectName(u"line0")
        self.line0.setGeometry(QRect(290, 240, 181, 41))
        self.line0.setMaxLength(30)
        self.line0.setAlignment(Qt.AlignCenter)
        self.enterPlayerX = QPushButton(self.centralwidget)
        self.enterPlayerX.setObjectName(u"enterPlayerX")
        self.enterPlayerX.setGeometry(QRect(80, 290, 75, 24))
        self.enterPlayer0 = QPushButton(self.centralwidget)
        self.enterPlayer0.setObjectName(u"enterPlayer0")
        self.enterPlayer0.setGeometry(QRect(350, 290, 75, 24))
        SetNameWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SetNameWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 22))
        SetNameWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SetNameWindow)
        self.statusbar.setObjectName(u"statusbar")
        SetNameWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SetNameWindow)

        QMetaObject.connectSlotsByName(SetNameWindow)
    # setupUi

    def retranslateUi(self, SetNameWindow):
        SetNameWindow.setWindowTitle(QCoreApplication.translate("SetNameWindow", u"\u041a\u0440\u0435\u0441\u0442\u0438\u043a\u0438-\u043d\u043e\u043b\u0438\u043a\u0438", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("SetNameWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u0435\u043d\u0430", None))
        self.startButton.setText(QCoreApplication.translate("SetNameWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0438\u0433\u0440\u0443", None))
        self.label_3.setText(QCoreApplication.translate("SetNameWindow", u"<html><head/><body><p>\u0418\u0433\u0440\u043e\u043a <span style=\" color:#1508c8;\">X</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("SetNameWindow", u"<html><head/><body><p>\u0418\u0433\u0440\u043e\u043a <span style=\" color:#ff0000;\">0</span></p></body></html>", None))
        self.enterPlayerX.setText(QCoreApplication.translate("SetNameWindow", u"\u0412\u0432\u043e\u0434", None))
        self.enterPlayer0.setText(QCoreApplication.translate("SetNameWindow", u"\u0412\u0432\u043e\u0434", None))
    # retranslateUi

