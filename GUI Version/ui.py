from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import config



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

        if config.language == "ru":
          self.retranslateUiRu(MainWindow)
        else:
          self.retranslateUiEn(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUiRu(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Weather by kindast", None))
        self.wbtn.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.lineedit.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.wbtnr.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0437\u043d\u0430\u0442\u044c \u043f\u043e\u0433\u043e\u0434\u0443", None))

    def retranslateUiEn(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Weather by kindast", None))
        self.wbtn.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.lineedit.setText(QCoreApplication.translate("MainWindow", u"City", None))
        self.wbtnr.setText(QCoreApplication.translate("MainWindow", u"Get weather", None))



class Ui_WeatherWindow(object):
    def setupUiw(self, WeatherWindow):
        if not WeatherWindow.objectName():
            WeatherWindow.setObjectName(u"WeatherWindow")
        WeatherWindow.resize(400, 190)
        WeatherWindow.setMinimumSize(QSize(400, 190))
        WeatherWindow.setMaximumSize(QSize(400, 190))
        icon = QIcon()
        icon.addFile(u"icons/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        WeatherWindow.setWindowIcon(icon)
        #Palette
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        #Font 25
        font = QFont()
        font.setFamily(u"Yandex Sans Text Medium")
        font.setPointSize(25)
        #Font 20
        font1 = QFont()
        font1.setFamily(u"Yandex Sans Text Medium")
        font1.setPointSize(20)
        #Font 14
        font2 = QFont()
        font2.setFamily(u"Yandex Sans Text Medium")
        font2.setPointSize(14)
        #City
        self.citylbl = QLabel(WeatherWindow)
        self.citylbl.setObjectName(u"citylbl")
        self.citylbl.setGeometry(QRect(0, 0, 400, 50))
        self.citylbl.setPalette(palette)
        self.citylbl.setFont(font)
        self.citylbl.setTextFormat(Qt.AutoText)
        self.citylbl.setAlignment(Qt.AlignCenter)
        #Temperature
        self.templbl = QLabel(WeatherWindow)
        self.templbl.setObjectName(u"templbl")
        if config.language == "ru":
          self.templbl.setGeometry(QRect(59, 70, 71, 31))
        else:
          self.templbl.setGeometry(QRect(4, 70, 161, 31))
        self.templbl.setPalette(palette)
        self.templbl.setFont(font1)
        self.templbl.setAlignment(Qt.AlignRight)
        #Weather
        self.weatherlbl = QLabel(WeatherWindow)
        self.weatherlbl.setObjectName(u"weatherlbl")
        self.weatherlbl.setGeometry(QRect(0, 40, 400, 31))
        self.weatherlbl.setPalette(palette)
        self.weatherlbl.setFont(font2)
        self.weatherlbl.setAlignment(Qt.AlignCenter)
        #Feels like
        self.feelslbl = QLabel(WeatherWindow)
        self.feelslbl.setObjectName(u"feelslbl")
        if config.language == "ru":
          self.feelslbl.setGeometry(QRect(135, 75, 251, 21))
        else:
          self.feelslbl.setGeometry(QRect(170, 75, 231, 21))
        self.feelslbl.setPalette(palette)
        self.feelslbl.setFont(font2)
        self.feelslbl.setAlignment(Qt.AlignLeft)
        #Background
        self.bg = QLabel(WeatherWindow)
        self.bg.setObjectName(u"bg")
        self.bg.setGeometry(QRect(0, 0, 411, 211))
        self.bg.setPixmap(QPixmap(u"icons/background.jpg"))
        self.bg.setScaledContents(True)
        #Windspeed
        self.windspeed = QLabel(WeatherWindow)
        self.windspeed.setObjectName(u"windspeed")
        if config.language == "ru":
          self.windspeed.setGeometry(QRect(13, 110, 211, 21))
        else:
          self.windspeed.setGeometry(QRect(2, 110, 191, 21))
        self.windspeed.setPalette(palette)
        self.windspeed.setFont(font2)
        self.windspeed.setAlignment(Qt.AlignRight)
        #Air Humidity
        self.airhumidity = QLabel(WeatherWindow)
        self.airhumidity.setObjectName(u"airhumidity")
        if config.language == "ru":
          self.airhumidity.setGeometry(QRect(233, 110, 161, 20))
        else:
          self.airhumidity.setGeometry(QRect(221, 110, 181, 20))
        self.airhumidity.setPalette(palette)
        self.airhumidity.setFont(font2)
        self.airhumidity.setAlignment(Qt.AlignLeft)
        #Pressure
        self.pressure = QLabel(WeatherWindow)
        self.pressure.setObjectName(u"pressure")
        self.pressure.setGeometry(QRect(4, 140, 391, 20))
        self.pressure.setPalette(palette)
        self.pressure.setFont(font2)
        self.pressure.setAlignment(Qt.AlignCenter)
        
        self.bg.raise_()
        self.citylbl.raise_()
        self.feelslbl.raise_()
        self.templbl.raise_()
        self.weatherlbl.raise_()
        self.windspeed.raise_()
        self.airhumidity.raise_()
        self.pressure.raise_()

        if config.language == "ru":
          self.retranslateUiRu(WeatherWindow)
        else:
          self.retranslateUiEn(WeatherWindow)

        QMetaObject.connectSlotsByName(WeatherWindow)
    # setupUi

    def retranslateUiRu(self, WeatherWindow):
        WeatherWindow.setWindowTitle(QCoreApplication.translate("WeatherWindow", u"Form", None))
        self.citylbl.setText(QCoreApplication.translate("WeatherWindow", u"\u0412\u0430\u0448 \u0433\u043e\u0440\u043e\u0434", None))
        self.templbl.setText(QCoreApplication.translate("WeatherWindow", u"0", None))
        self.weatherlbl.setText(QCoreApplication.translate("WeatherWindow", u"\u041f\u043e\u0433\u043e\u0434\u0430", None))
        self.feelslbl.setText(QCoreApplication.translate("WeatherWindow", u"0", None))
        self.windspeed.setText(QCoreApplication.translate("WeatherWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u0432\u0435\u0442\u0440\u0430:", None))
        self.airhumidity.setText(QCoreApplication.translate("WeatherWindow", u"\u0412\u043b\u0430\u0436\u043d\u043e\u0441\u0442\u044c:", None))
        self.pressure.setText(QCoreApplication.translate("WeatherWindow", u"\u0414\u0430\u0432\u043b\u0435\u043d\u0438\u0435:", None))

    def retranslateUiEn(self, WeatherWindow):
        WeatherWindow.setWindowTitle(QCoreApplication.translate("WeatherWindow", u"Form", None))
        self.citylbl.setText(QCoreApplication.translate("WeatherWindow", u"\u0412\u0430\u0448 \u0433\u043e\u0440\u043e\u0434", None))
        self.templbl.setText(QCoreApplication.translate("WeatherWindow", u"0", None))
        self.weatherlbl.setText(QCoreApplication.translate("WeatherWindow", u"\u041f\u043e\u0433\u043e\u0434\u0430", None))
        self.feelslbl.setText(QCoreApplication.translate("WeatherWindow", u"0", None))
        self.windspeed.setText(QCoreApplication.translate("WeatherWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u0432\u0435\u0442\u0440\u0430:", None))
        self.airhumidity.setText(QCoreApplication.translate("WeatherWindow", u"\u0412\u043b\u0430\u0436\u043d\u043e\u0441\u0442\u044c:", None))
        self.pressure.setText(QCoreApplication.translate("WeatherWindow", u"\u0414\u0430\u0432\u043b\u0435\u043d\u0438\u0435:", None))

