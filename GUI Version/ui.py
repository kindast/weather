from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

#Config
try:
  config = open("config.txt", mode="r")
  text = config.read()
  language = text.partition('"')[2].partition('"')[2].partition('"')[2].partition('"')[2].partition('"')[2].partition('"')[0]
  config.close()
except FileNotFoundError:
  weatherAPI = "e369944a-4f01-4956-88d0-054f68144487"
  geocoderAPI = "db527ae8-6405-44df-91da-5cec4d049af6"
  language = "en"
  config = open("config.txt", mode="w")

  wapi = 'weatherAPI = "e369944a-4f01-4956-88d0-054f68144487"'
  gapi = 'geocoderAPI = "db527ae8-6405-44df-91da-5cec4d049af6"'
  lang = 'language = "en"'

  config.write(wapi + "\n" + gapi + "\n" + lang)
  config.close()

class MainUI(object):
    def setupMainUI(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(463, 92)
        Main.setMinimumSize(QSize(463, 92))
        Main.setMaximumSize(QSize(463, 92))
        icon = QIcon()
        icon.addFile(u"icons/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Main.setWindowIcon(icon)
        #Font 16
        font = QFont()
        font.setFamily(u"Yandex Sans Text")
        font.setPointSize(16)
        #Autolocation
        self.wbtn = QPushButton(Main)
        self.wbtn.setObjectName(u"wbtn")
        self.wbtn.setGeometry(QRect(380, 10, 31, 31))
        self.wbtn.setFont(font)
        self.wbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.wbtn.setAcceptDrops(False)
        self.wbtn.setCheckable(False)
        #City
        self.lineedit = QLineEdit(Main)
        self.lineedit.setObjectName(u"lineedit")
        self.lineedit.setGeometry(QRect(60, 10, 351, 31))
        self.lineedit.setFont(font)
        self.lineedit.setFrame(True)
        self.lineedit.setEchoMode(QLineEdit.Normal)
        #GetWeather
        self.wbtnr = QPushButton(Main)
        self.wbtnr.setObjectName(u"wbtnr")
        self.wbtnr.setGeometry(QRect(60, 50, 351, 31))
        self.wbtnr.setFont(font)
        self.wbtnr.setCursor(QCursor(Qt.PointingHandCursor))
        #Settings
        self.setbtn = QPushButton(Main)
        self.setbtn.setObjectName(u"setbtn")
        self.setbtn.setGeometry(QRect(420, 10, 31, 31))
        icon1 = QIcon()
        icon1.addFile(u"icons/settings.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.setbtn.setIcon(icon1)
        self.setbtn.setIconSize(QSize(25, 25))
        self.setbtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.lineedit.raise_()
        self.wbtnr.raise_()
        self.wbtn.raise_()
        self.setbtn.raise_()

        if language == "ru":
          self.TextMainRu(Main)
        else:
          self.TextMainEn(Main)

        QMetaObject.connectSlotsByName(Main)

    def TextMainRu(self, Main):
        Main.setWindowTitle("Weather by kindast")
        self.wbtn.setText("A")
        self.lineedit.setPlaceholderText("Город")
        self.wbtnr.setText("Узнать погоду")

    def TextMainEn(self, Main):
        Main.setWindowTitle("Weather by kindast")
        self.wbtn.setText("A")
        self.lineedit.setPlaceholderText("City")
        self.wbtnr.setText("Get weather")

class WeatherUI(object):
    def setupWeatherUI(self, Weather):
        if not Weather.objectName():
            Weather.setObjectName(u"Weather")
        Weather.resize(400, 190)
        Weather.setMinimumSize(QSize(400, 190))
        Weather.setMaximumSize(QSize(400, 190))
        icon = QIcon()
        icon.addFile(u"icons/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Weather.setWindowIcon(icon)
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
        self.citylbl = QLabel(Weather)
        self.citylbl.setObjectName(u"citylbl")
        self.citylbl.setGeometry(QRect(0, 0, 400, 50))
        self.citylbl.setPalette(palette)
        self.citylbl.setFont(font)
        self.citylbl.setTextFormat(Qt.AutoText)
        self.citylbl.setAlignment(Qt.AlignCenter)
        #Temperature
        self.templbl = QLabel(Weather)
        self.templbl.setObjectName(u"templbl")
        if language == "ru":
          self.templbl.setGeometry(QRect(59, 70, 71, 31))
        else:
          self.templbl.setGeometry(QRect(4, 70, 161, 31))
        self.templbl.setPalette(palette)
        self.templbl.setFont(font1)
        self.templbl.setAlignment(Qt.AlignRight)
        #Weather
        self.weatherlbl = QLabel(Weather)
        self.weatherlbl.setObjectName(u"weatherlbl")
        self.weatherlbl.setGeometry(QRect(0, 40, 400, 31))
        self.weatherlbl.setPalette(palette)
        self.weatherlbl.setFont(font2)
        self.weatherlbl.setAlignment(Qt.AlignCenter)
        #Feels like
        self.feelslbl = QLabel(Weather)
        self.feelslbl.setObjectName(u"feelslbl")
        if language == "ru":
          self.feelslbl.setGeometry(QRect(135, 75, 251, 21))
        else:
          self.feelslbl.setGeometry(QRect(170, 75, 231, 21))
        self.feelslbl.setPalette(palette)
        self.feelslbl.setFont(font2)
        self.feelslbl.setAlignment(Qt.AlignLeft)
        #Background
        self.bg = QLabel(Weather)
        self.bg.setObjectName(u"bg")
        self.bg.setGeometry(QRect(0, 0, 411, 211))
        self.bg.setPixmap(QPixmap(u"icons/background.jpg"))
        self.bg.setScaledContents(True)
        #Windspeed
        self.windspeed = QLabel(Weather)
        self.windspeed.setObjectName(u"windspeed")
        if language == "ru":
          self.windspeed.setGeometry(QRect(13, 110, 211, 21))
        else:
          self.windspeed.setGeometry(QRect(2, 110, 191, 21))
        self.windspeed.setPalette(palette)
        self.windspeed.setFont(font2)
        self.windspeed.setAlignment(Qt.AlignRight)
        #Air Humidity
        self.airhumidity = QLabel(Weather)
        self.airhumidity.setObjectName(u"airhumidity")
        if language == "ru":
          self.airhumidity.setGeometry(QRect(233, 110, 161, 20))
        else:
          self.airhumidity.setGeometry(QRect(221, 110, 181, 20))
        self.airhumidity.setPalette(palette)
        self.airhumidity.setFont(font2)
        self.airhumidity.setAlignment(Qt.AlignLeft)
        #Pressure
        self.pressure = QLabel(Weather)
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

        QMetaObject.connectSlotsByName(Weather)

class SettingsUI(object):
    def setupSettingsUI(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(251, 161)
        Settings.setMinimumSize(QSize(251, 161))
        Settings.setMaximumSize(QSize(251, 161))
        icon = QIcon()
        icon.addFile(u"icons/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Settings.setWindowIcon(icon)
        #Font 10
        font = QFont()
        font.setFamily(u"Yandex Sans Text")
        font.setPointSize(10)
        #Font 8
        font1 = QFont()
        font1.setFamily(u"Yandex Sans Text")
        #Save
        self.savebtn = QPushButton(Settings)
        self.savebtn.setObjectName(u"savebtn")
        self.savebtn.setGeometry(QRect(80, 130, 81, 23))
        self.savebtn.setFont(font)
        #API Yandex.Weather
        self.apiweather = QLineEdit(Settings)
        self.apiweather.setObjectName(u"apiweather")
        self.apiweather.setGeometry(QRect(10, 20, 231, 20))
        self.apiweather.setFont(font1)
        self.apiweather.setStyleSheet(u"")
        self.apiweather.setFrame(True)
        self.apiweather.setAlignment(Qt.AlignCenter)
        #API Yandex.Geocoder
        self.apigeocoder = QLineEdit(Settings)
        self.apigeocoder.setObjectName(u"apigeocoder")
        self.apigeocoder.setGeometry(QRect(10, 60, 231, 20))
        self.apigeocoder.setFont(font1)
        self.apigeocoder.setStyleSheet(u"")
        self.apigeocoder.setFrame(True)
        self.apigeocoder.setAlignment(Qt.AlignCenter)
        #Labels
        self.apiglbl = QLabel(Settings)
        self.apiglbl.setObjectName(u"apiglbl")
        self.apiglbl.setGeometry(QRect(10, 40, 231, 21))
        self.apiglbl.setFont(font)
        self.apiglbl.setAlignment(Qt.AlignCenter)
        self.apiwlbl = QLabel(Settings)
        self.apiwlbl.setObjectName(u"apiwlbl")
        self.apiwlbl.setGeometry(QRect(10, 0, 231, 21))
        self.apiwlbl.setFont(font)
        self.apiwlbl.setAlignment(Qt.AlignCenter)
        self.langlbl = QLabel(Settings)
        self.langlbl.setObjectName(u"langlbl")
        self.langlbl.setGeometry(QRect(10, 80, 231, 21))
        self.langlbl.setFont(font)
        self.langlbl.setAlignment(Qt.AlignCenter)
        #languages
        self.langbox = QComboBox(Settings)
        self.langbox.setObjectName(u"langbox")
        self.langbox.setGeometry(QRect(10, 100, 231, 22))
        self.langbox.setFont(font1)

        if language == "ru":
          self.TextSettingsRu(Settings)
        else:
          self.TextSettingsEn(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def TextSettingsEn(self, Settings):
        Settings.setWindowTitle("Settings")
        self.savebtn.setText("Save")
        self.apiglbl.setText("API Key for Yandex.Geocoder")
        self.apiwlbl.setText("API Key for Yandex.Weather")
        self.langlbl.setText("Language")

    def TextSettingsRu(self, Settings):
        Settings.setWindowTitle("Настройки")
        self.savebtn.setText("Сохранить")
        self.apiglbl.setText("API Ключ Яндекс.Геокодера")
        self.apiwlbl.setText("API Ключ Яндекс.Погоды")
        self.langlbl.setText("Язык")