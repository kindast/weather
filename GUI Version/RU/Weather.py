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
                       params={"lang": "ru"}
                       )
    data = res.json()
    return data['city']

def get_coords(city):
    res = requests.get("https://geocode-maps.yandex.ru/1.x",
                       params={"geocode": city,
                               "apikey": "db527ae8-6405-44df-91da-5cec4d049af6",
                               "sco": "latlong",
                               "format": "json",
                               "results": "1",
                               "lang": "ru_RU"}
                       )
    data = res.json()
    coords = ((((((data["response"])["GeoObjectCollection"])["featureMember"])[0])["GeoObject"])["Point"])["pos"].partition(" ")
    coords = {"lat": coords[0], "lon": coords[2]}
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
    # Traslate
    if weather["condition"] == "clear":
        weather["condition"] = "Ясно"
    elif weather["condition"] == "cloudy":
        weather["condition"] = "Облачно с прояснениями"
    elif weather["condition"] == "overcast":
        weather["condition"] = "Пасмурно"
    elif weather["condition"] == "partly-cloudy":
        weather["condition"] = "Малооблачно"
    elif weather["condition"] == "partly-cloudy-and-light-rain":
        weather["condition"] = "Небольшой дождь"
    elif weather["condition"] == "partly-cloudy-and-rain":
        weather["condition"] = "Дождь"
    elif weather["condition"] == "overcast-and-rain":
        weather["condition"] = "Сильный дождь"
    elif weather["condition"] == "overcast-thunderstorms-with-rain":
        weather["condition"] = "Сильный дождь, гроза"
    elif (weather["condition"] == "cloudy-and-light-rain") or (weather["condition"] == "overcast-and-light-rain"):
        weather["condition"] = "Небольшой дождь"
    elif weather["condition"] == "cloudy-and-rain":
        weather["condition"] = "Дождь"
    elif weather["condition"] == "overcast-and-wet-snow":
        weather["condition"] = "Дождь со снегом"
    elif weather["condition"] == "partly-cloudy-and-light-snow":
        weather["condition"] = "Небольшой снег"
    elif weather["condition"] == "partly-cloudy-and-snow":
        weather["condition"] = "Снег"
    elif weather["condition"] == "overcast-and-wet-snow":
        weather["condition"] = "Дождь со снегом"
    return weather


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
        uiw.feelslbl.setText("Ощущается как: " + str(weather["feels_like"]) + "°С")
        uiw.windspeed.setText("Скорость ветра: " + str(weather["wind_speed"]) + " м/с")
        uiw.airhumidity.setText("Влажность: " + str(weather["humidity"]) + " %")
        uiw.pressure.setText("Давление: " + str(weather["pressure_mm"]) + " мм рт. ст.")

        WeatherWindow.show()
        WeatherWindow.exec()
    except IndexError:
        mbox = QMessageBox()
        mbox.setWindowTitle("Ошибка")
        mbox.setText("Неправильно введён город или нет подключения к Интернету")
        icon = QIcon()
        icon.addFile(u"icons/error.png", QSize(), QIcon.Normal, QIcon.Off)
        mbox.setWindowIcon(icon)
        mbox.show()
        mbox.exec()

ui.wbtn.clicked.connect(auto_city)
ui.wbtnr.clicked.connect(weather)

sys.exit(app.exec_())
