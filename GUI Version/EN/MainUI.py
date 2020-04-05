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
        MainWindow.resize(463, 133)
        MainWindow.setMinimumSize(QSize(463, 67))
        MainWindow.setMaximumSize(QSize(463, 133))
        icon = QIcon()
        icon.addFile(u"icons/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.line = QFrame(MainWindow)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-10, 50, 481, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.wbtn = QPushButton(MainWindow)
        self.wbtn.setObjectName(u"wbtn")
        self.wbtn.setGeometry(QRect(10, 10, 441, 41))
        font = QFont()
        font.setFamily(u"Yandex Sans Text Medium")
        font.setPointSize(16)
        font.setWeight(50)
        self.wbtn.setFont(font)
        self.lineedit = QLineEdit(MainWindow)
        self.lineedit.setObjectName(u"lineedit")
        self.lineedit.setGeometry(QRect(80, 70, 291, 21))
        self.wbtnr = QPushButton(MainWindow)
        self.wbtnr.setObjectName(u"wbtnr")
        self.wbtnr.setGeometry(QRect(110, 98, 231, 31))
        self.wbtnr.setFont(font)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Weather by kindast")
        self.wbtn.setText("Auto location")
        self.wbtnr.setText("Get weather")
    # retranslateUi
