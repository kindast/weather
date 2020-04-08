from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *
from MainUI import Ui_MainWindow
from WeatherUI import Ui_WeatherWindow
import sys
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
    res = requests.get("http://www.datasciencetoolkit.org/maps/api/geocode/json",
                       params={"address": city}
                       )
    data = res.json()
    data = (((data["results"])[0])["geometry"])["location"]
    coords = {"lat": data["lat"], "lon": data["lng"]}
    return coords

def get_weather(lat, lon):
    YandexAPIkey = "0c0ec0c2-2aeb-4710-9e72-be9f4127ad6f"
    res = requests.get("https://api.weather.yandex.ru/v1/forecast/",
                       params={"lat": lat, "lon": lon,
                               "lang": "ru_RU", "limit": 1},
                       headers={"X-Yandex-API-Key": YandexAPIkey}
                       )
    data = res.json()
    weather = data["fact"]
    return weather


def autoweather(self):
    city = get_city()
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
    uiw.pressure.setText("Pressure: " + str(weather["pressure_mm"]) + " mm Hg. Art.")

    WeatherWindow.show()
    WeatherWindow.exec()

def handweather(self):
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
        uiw.feelslbl.setText("Ощущается как: " + str(weather["feels_like"]) + "°С")
        uiw.windspeed.setText("Скорость ветра: " + str(weather["wind_speed"]) + " м/с")
        uiw.airhumidity.setText("Влажность: " + str(weather["humidity"]) + " %")
        uiw.pressure.setText("Давление: " + str(weather["pressure_mm"]) + " мм рт. ст.")

        WeatherWindow.show()
        WeatherWindow.exec()
    except IndexError:
        mbox = QMessageBox()
        mbox.setWindowTitle("Ошибка")
        mbox.setText("Неправильно введён город")
        mbox.show()
        mbox.exec()

ui.wbtn.clicked.connect(autoweather)
ui.wbtnr.clicked.connect(handweather)

sys.exit(app.exec_())
