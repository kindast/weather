from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(463, 92)
        MainWindow.setMinimumSize(QSize(463, 92))
        MainWindow.setMaximumSize(QSize(463, 92))
        #Icon
        icon = QIcon()
        icon.addFile(u"icons/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        #Font 16
        font = QFont()
        font.setFamily(u"Yandex Sans Text")
        font.setPointSize(16)
        #Autolocation
        self.wbtn = QPushButton(MainWindow)
        self.wbtn.setObjectName(u"wbtn")
        self.wbtn.setGeometry(QRect(380, 10, 31, 31))
        self.wbtn.setFont(font)
        self.wbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.wbtn.setAcceptDrops(False)
        self.wbtn.setCheckable(False)
        #City
        self.lineedit = QLineEdit(MainWindow)
        self.lineedit.setObjectName(u"lineedit")
        self.lineedit.setGeometry(QRect(60, 10, 351, 31))
        self.lineedit.setFont(font)
        self.lineedit.setFrame(True)
        self.lineedit.setEchoMode(QLineEdit.Normal)
        #GetWeather
        self.wbtnr = QPushButton(MainWindow)
        self.wbtnr.setObjectName(u"wbtnr")
        self.wbtnr.setGeometry(QRect(60, 50, 351, 31))
        self.wbtnr.setFont(font)
        self.wbtnr.setCursor(QCursor(Qt.PointingHandCursor))
        self.lineedit.raise_()
        self.wbtnr.raise_()
        self.wbtn.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Weather by kindast", None))
        self.wbtn.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.lineedit.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.wbtnr.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0437\u043d\u0430\u0442\u044c \u043f\u043e\u0433\u043e\u0434\u0443", None))
    # retranslateUi

