# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_GameScreen(object):
    def setupUi(self, GameScreen):
        if not GameScreen.objectName():
            GameScreen.setObjectName(u"GameScreen")
        GameScreen.resize(500, 640)
        self.centralwidget = QWidget(GameScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(50, 160, 401, 304))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(100, 100))
        font = QFont()
        font.setPointSize(72)
        self.pushButton_2.setFont(font)

        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QSize(100, 100))
        self.pushButton_6.setFont(font)

        self.gridLayout.addWidget(self.pushButton_6, 2, 1, 1, 1)

        self.pushButton_1 = QPushButton(self.gridLayoutWidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        self.pushButton_1.setMinimumSize(QSize(100, 100))
        self.pushButton_1.setFont(font)

        self.gridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QSize(100, 100))
        self.pushButton_4.setFont(font)

        self.gridLayout.addWidget(self.pushButton_4, 0, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QSize(100, 100))
        self.pushButton_5.setFont(font)

        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QSize(100, 100))
        self.pushButton_3.setFont(font)

        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QSize(100, 100))
        self.pushButton_7.setFont(font)

        self.gridLayout.addWidget(self.pushButton_7, 0, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMinimumSize(QSize(100, 100))
        self.pushButton_8.setFont(font)

        self.gridLayout.addWidget(self.pushButton_8, 1, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMinimumSize(QSize(100, 100))
        self.pushButton_9.setFont(font)

        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.exitButton = QPushButton(self.centralwidget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(190, 560, 111, 31))
        self.resetButton = QPushButton(self.centralwidget)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setGeometry(QRect(190, 480, 111, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 20, 71, 21))
        font1 = QFont()
        font1.setPointSize(18)
        self.label.setFont(font1)
        self.playerX = QLabel(self.centralwidget)
        self.playerX.setObjectName(u"playerX")
        self.playerX.setGeometry(QRect(80, 50, 71, 21))
        font2 = QFont()
        font2.setPointSize(12)
        self.playerX.setFont(font2)
        self.playerX.setAlignment(Qt.AlignCenter)
        self.player0 = QLabel(self.centralwidget)
        self.player0.setObjectName(u"player0")
        self.player0.setGeometry(QRect(340, 50, 71, 21))
        self.player0.setFont(font2)
        self.player0.setAlignment(Qt.AlignCenter)
        self.scorePlayerX = QLabel(self.centralwidget)
        self.scorePlayerX.setObjectName(u"scorePlayerX")
        self.scorePlayerX.setGeometry(QRect(110, 70, 31, 21))
        font3 = QFont()
        font3.setPointSize(16)
        self.scorePlayerX.setFont(font3)
        self.scorePlayer0 = QLabel(self.centralwidget)
        self.scorePlayer0.setObjectName(u"scorePlayer0")
        self.scorePlayer0.setGeometry(QRect(370, 70, 31, 21))
        self.scorePlayer0.setFont(font3)
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(190, 520, 111, 31))
        GameScreen.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(GameScreen)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 22))
        GameScreen.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(GameScreen)
        self.statusbar.setObjectName(u"statusbar")
        GameScreen.setStatusBar(self.statusbar)

        self.retranslateUi(GameScreen)

        QMetaObject.connectSlotsByName(GameScreen)
    # setupUi

    def retranslateUi(self, GameScreen):
        self.pushButton_2.setText("")
        self.pushButton_6.setText("")
        self.pushButton_1.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_3.setText("")
        self.pushButton_7.setText("")
        self.pushButton_8.setText("")
        self.pushButton_9.setText("")
        self.exitButton.setText(QCoreApplication.translate("GameScreen", u"\u0412\u044b\u0439\u0442\u0438 \u0438\u0437 \u0438\u0433\u0440\u044b", None))
        self.resetButton.setText(QCoreApplication.translate("GameScreen", u"\u0417\u0430\u043d\u043e\u0432\u043e", None))
        self.label.setText(QCoreApplication.translate("GameScreen", u"\u0421\u0447\u0451\u0442:", None))
        self.playerX.setText(QCoreApplication.translate("GameScreen", u"\u0418\u0433\u0440\u043e\u043a X:", None))
        self.player0.setText(QCoreApplication.translate("GameScreen", u"\u0418\u0433\u0440\u043e\u043a 0:", None))
        self.scorePlayerX.setText(QCoreApplication.translate("GameScreen", u"0", None))
        self.scorePlayer0.setText(QCoreApplication.translate("GameScreen", u"0", None))
        self.backButton.setText(QCoreApplication.translate("GameScreen", u"\u041d\u0430\u0437\u0430\u0434", None))
        pass
    # retranslateUi

