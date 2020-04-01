from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *
from weather_ui_en import Ui_MainWindow
import sys
import requests

app = QApplication(sys.argv)

MainWindow = QWidget()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

def weather():
    #Get city
    res0 = requests.get("http://ip-api.com/json?fields=country,city",
                       params={"lang": "en"}
                       )
    data0 = res0.json()
    city = data0["city"]
    #Get coords
    res1 = requests.get("http://www.datasciencetoolkit.org/maps/api/geocode/json",
                       params={"address": city}
                       )
    data1 = res1.json()
    data1 = (((data1["results"])[0])["geometry"])["location"]
    #Get weather
    YandexAPIkey = "0c0ec0c2-2aeb-4710-9e72-be9f4127ad6f"
    res2 = requests.get("https://api.weather.yandex.ru/v1/forecast/",
                       params={"lat": data1["lat"], "lon": data1["lng"], "lang": "ru_RU", "limit": 1},
                       headers={"X-Yandex-API-Key": YandexAPIkey}
                       )
    data2 = res2.json()
    weather = data2["fact"]

    WeatherWindow = QWidget()

    icon = QIcon()
    icon.addFile(u"icons/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
    WeatherWindow.setWindowIcon(icon)

    WeatherWindow.setWindowTitle(city)

    WeatherWindow.show()
    WeatherWindow.exec()

ui.wbtn.clicked.connect(weather)

sys.exit(app.exec_())
