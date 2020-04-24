from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *
from MainUI import Ui_MainWindow
from WeatherUI import Ui_WeatherWindow
import sys, config
import requests

app = QApplication(sys.argv)

MainWindow = QWidget()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

def get_city():
    res = requests.get("http://ip-api.com/json?fields=country,city",
                       params={"lang": "en"}
                       )
    data = res.json()
    return data['city']

def get_coords(city):
    res = requests.get("https://geocode-maps.yandex.ru/1.x",
                       params={"geocode": city,
                               "apikey": config.GeocoderAPIKey,
                               "sco": "latlong",
                               "format": "json",
                               "results": "1",
                               "lang": "en_RU"}
                       )
    if not res.status_code == 200:
      error("Wrong API key for Yandex.Geocoder")
    else:
      data = res.json()
      coords = ((((((data["response"])["GeoObjectCollection"])["featureMember"])[0])["GeoObject"])["Point"])["pos"].partition(" ")
      coords = {"lat": coords[2], "lon": coords[0]}
      return coords

def get_weather(lat, lon):
    res = requests.get("https://api.weather.yandex.ru/v1/forecast/",
                       params={"lat": lat, "lon": lon,
                               "lang": "en_US", "limit": 1},
                       headers={"X-Yandex-API-Key": config.WeatherAPIKey}
                       )
    if not res.status_code == 200:
      error("Wrong API key for Yandex.Weathers")
    else:
      data = res.json()
      return data["fact"]

def error(text):
    mbox = QMessageBox()
    mbox.setWindowTitle("Error")
    mbox.setText(text)
    icon = QIcon()
    icon.addFile(u"icons/error.png", QSize(), QIcon.Normal, QIcon.Off)
    mbox.setWindowIcon(icon)
    mbox.show()
    mbox.exec()

def auto_city(self):
    city = get_city()
    ui.lineedit.setText(city)

def weather(self):
    try:
        city = ui.lineedit.text()
        coords = get_coords(city)
        weather = get_weather(coords["lat"], coords["lon"])

        WeatherWindow = QWidget()

        uiw = Ui_WeatherWindow()
        uiw.setupUiw(WeatherWindow)
        WeatherWindow.setWindowTitle(city)

        uiw.citylbl.setText(city)
        uiw.weatherlbl.setText(weather["condition"])
        uiw.templbl.setText(str(weather["temp"]) + "°С")
        uiw.feelslbl.setText("Feels like: " + str(weather["feels_like"]) + "°С")
        uiw.windspeed.setText("Wind speed: " + str(weather["wind_speed"]) + " m/s")
        uiw.airhumidity.setText("Air humidity: " + str(weather["humidity"]) + " %")
        uiw.pressure.setText("Pressure: " + str(weather["pressure_mm"]) + " mm Hg.")

        WeatherWindow.show()
        WeatherWindow.exec()
    except IndexError:
      error("The city was entered incorrectly or there is no Internet connection")

ui.wbtn.clicked.connect(auto_city)
ui.wbtnr.clicked.connect(weather)

sys.exit(app.exec_())
