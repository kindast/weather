from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *
from weather_ui_en import Ui_MainWindow
from info_en import Ui_WeatherWindow
import sys
import requests

app = QApplication(sys.argv)

MainWindow = QWidget()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

def weather(self):
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

    uiw = Ui_WeatherWindow()
    uiw.setupUiw(WeatherWindow)
    WeatherWindow.setWindowTitle(city)

    uiw.citylbl.setText(city)
    uiw.weatherlbl.setText(weather["condition"].title())
    uiw.templbl.setText(str(weather["temp"]))
    uiw.feelslbl.setText(str(weather["feels_like"]))
    uiw.speedlbl.setText(str(weather["wind_speed"]))
    uiw.humlbl.setText(str(weather["humidity"]))
    uiw.preslbl.setText(str(weather["pressure_mm"]))

    WeatherWindow.show()
    WeatherWindow.exec()

def github():
    git = QWidget()

    font = QFont()
    font.setFamily(u"Yandex Sans Text Medium")
    font.setPointSize(20)

    label = QLabel(git)
    label.setText("<a href='https://github.com/kindast/weather'>Go to github</a>")
    label.setOpenExternalLinks(True)
    label.setFont(font)

    git.setWindowTitle("Github")
    git.resize(158, 35)
    git.setMinimumSize(QSize(158, 35))
    git.show()
    git.exec()

ui.wbtn.clicked.connect(weather)
ui.gitbtn.clicked.connect(github)

sys.exit(app.exec_())
