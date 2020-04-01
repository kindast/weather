from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(463, 67)
        MainWindow.setMinimumSize(QSize(463, 67))
        MainWindow.setMaximumSize(QSize(463, 67))
        icon = QIcon()
        icon.addFile(u"icons/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 461, 61))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.wbtn = QPushButton(self.horizontalLayoutWidget)
        self.wbtn.setObjectName(u"wbtn")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.wbtn.setFont(font)

        self.horizontalLayout.addWidget(self.wbtn)

        self.gitbtn = QPushButton(self.horizontalLayoutWidget)
        self.gitbtn.setObjectName(u"gitbtn")
        icon1 = QIcon()
        icon1.addFile(u"icons/git.png", QSize(), QIcon.Normal, QIcon.Off)
        self.gitbtn.setIcon(icon1)
        self.gitbtn.setIconSize(QSize(132, 33))

        self.horizontalLayout.addWidget(self.gitbtn)

        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"Weather by kindast", None))
        self.wbtn.setText("Get weather")
        self.gitbtn.setText("")
    # retranslateUi
