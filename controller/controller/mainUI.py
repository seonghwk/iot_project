# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.commandLabel = QLabel(self.centralwidget)
        self.commandLabel.setObjectName(u"commandLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.commandLabel.sizePolicy().hasHeightForWidth())
        self.commandLabel.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.commandLabel, 0, 0, 1, 1)

        self.sensingLabel = QLabel(self.centralwidget)
        self.sensingLabel.setObjectName(u"sensingLabel")
        sizePolicy1.setHeightForWidth(self.sensingLabel.sizePolicy().hasHeightForWidth())
        self.sensingLabel.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.sensingLabel, 0, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.rightButton = QPushButton(self.centralwidget)
        self.rightButton.setObjectName(u"rightButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.rightButton.sizePolicy().hasHeightForWidth())
        self.rightButton.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.rightButton, 1, 2, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame, 1, 3, 1, 1)

        self.stopButton = QPushButton(self.centralwidget)
        self.stopButton.setObjectName(u"stopButton")
        sizePolicy2.setHeightForWidth(self.stopButton.sizePolicy().hasHeightForWidth())
        self.stopButton.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.stopButton, 1, 5, 1, 1)

        self.leftButton = QPushButton(self.centralwidget)
        self.leftButton.setObjectName(u"leftButton")
        sizePolicy2.setHeightForWidth(self.leftButton.sizePolicy().hasHeightForWidth())
        self.leftButton.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.leftButton, 1, 0, 1, 1)

        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        sizePolicy2.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.startButton, 1, 4, 1, 1)

        self.midButton = QPushButton(self.centralwidget)
        self.midButton.setObjectName(u"midButton")
        sizePolicy2.setHeightForWidth(self.midButton.sizePolicy().hasHeightForWidth())
        self.midButton.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.midButton, 1, 1, 1, 1)

        self.goButton = QPushButton(self.centralwidget)
        self.goButton.setObjectName(u"goButton")
        sizePolicy2.setHeightForWidth(self.goButton.sizePolicy().hasHeightForWidth())
        self.goButton.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.goButton, 0, 1, 1, 1)

        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setObjectName(u"backButton")
        sizePolicy2.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.backButton, 2, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 2)

        self.sensingText = QPlainTextEdit(self.centralwidget)
        self.sensingText.setObjectName(u"sensingText")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sensingText.sizePolicy().hasHeightForWidth())
        self.sensingText.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.sensingText, 1, 1, 1, 1)

        self.logText = QPlainTextEdit(self.centralwidget)
        self.logText.setObjectName(u"logText")
        sizePolicy3.setHeightForWidth(self.logText.sizePolicy().hasHeightForWidth())
        self.logText.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setFamilies([u"D2Coding"])
        self.logText.setFont(font)

        self.gridLayout_2.addWidget(self.logText, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 787, 36))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.startButton.clicked.connect(MainWindow.start)
        self.stopButton.clicked.connect(MainWindow.stop)
        self.goButton.clicked.connect(MainWindow.go)
        self.rightButton.clicked.connect(MainWindow.right)
        self.backButton.clicked.connect(MainWindow.back)
        self.leftButton.clicked.connect(MainWindow.left)
        self.midButton.clicked.connect(MainWindow.mid)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.commandLabel.setText(QCoreApplication.translate("MainWindow", u"command Table", None))
        self.sensingLabel.setText(QCoreApplication.translate("MainWindow", u"sensing Table", None))
        self.rightButton.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.leftButton.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.midButton.setText(QCoreApplication.translate("MainWindow", u"Mid", None))
        self.goButton.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(787, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.commandLabel = QLabel(self.centralwidget)
        self.commandLabel.setObjectName(u"commandLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.commandLabel.sizePolicy().hasHeightForWidth())
        self.commandLabel.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.commandLabel, 0, 0, 1, 1)

        self.sensingLabel = QLabel(self.centralwidget)
        self.sensingLabel.setObjectName(u"sensingLabel")
        sizePolicy1.setHeightForWidth(self.sensingLabel.sizePolicy().hasHeightForWidth())
        self.sensingLabel.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.sensingLabel, 0, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.rightButton = QPushButton(self.centralwidget)
        self.rightButton.setObjectName(u"rightButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.rightButton.sizePolicy().hasHeightForWidth())
        self.rightButton.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.rightButton, 1, 2, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame, 1, 3, 1, 1)

        self.stopButton = QPushButton(self.centralwidget)
        self.stopButton.setObjectName(u"stopButton")
        sizePolicy2.setHeightForWidth(self.stopButton.sizePolicy().hasHeightForWidth())
        self.stopButton.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.stopButton, 1, 5, 1, 1)

        self.leftButton = QPushButton(self.centralwidget)
        self.leftButton.setObjectName(u"leftButton")
        sizePolicy2.setHeightForWidth(self.leftButton.sizePolicy().hasHeightForWidth())
        self.leftButton.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.leftButton, 1, 0, 1, 1)

        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        sizePolicy2.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.startButton, 1, 4, 1, 1)

        self.midButton = QPushButton(self.centralwidget)
        self.midButton.setObjectName(u"midButton")
        sizePolicy2.setHeightForWidth(self.midButton.sizePolicy().hasHeightForWidth())
        self.midButton.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.midButton, 1, 1, 1, 1)

        self.goButton = QPushButton(self.centralwidget)
        self.goButton.setObjectName(u"goButton")
        sizePolicy2.setHeightForWidth(self.goButton.sizePolicy().hasHeightForWidth())
        self.goButton.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.goButton, 0, 1, 1, 1)

        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setObjectName(u"backButton")
        sizePolicy2.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.backButton, 2, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 2)

        self.sensingText = QPlainTextEdit(self.centralwidget)
        self.sensingText.setObjectName(u"sensingText")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sensingText.sizePolicy().hasHeightForWidth())
        self.sensingText.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.sensingText, 1, 1, 1, 1)

        self.logText = QPlainTextEdit(self.centralwidget)
        self.logText.setObjectName(u"logText")
        sizePolicy3.setHeightForWidth(self.logText.sizePolicy().hasHeightForWidth())
        self.logText.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setFamilies([u"D2Coding"])
        self.logText.setFont(font)

        self.gridLayout_2.addWidget(self.logText, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 787, 36))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.startButton.clicked.connect(MainWindow.start)
        self.stopButton.clicked.connect(MainWindow.stop)
        self.goButton.clicked.connect(MainWindow.go)
        self.rightButton.clicked.connect(MainWindow.right)
        self.backButton.clicked.connect(MainWindow.back)
        self.leftButton.clicked.connect(MainWindow.left)
        self.midButton.clicked.connect(MainWindow.mid)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.commandLabel.setText(QCoreApplication.translate("MainWindow", u"command Table", None))
        self.sensingLabel.setText(QCoreApplication.translate("MainWindow", u"sensing Table", None))
        self.rightButton.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.leftButton.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.midButton.setText(QCoreApplication.translate("MainWindow", u"Mid", None))
        self.goButton.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
    # retranslateUi

