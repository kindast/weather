from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *
from ui import Ui_MainWindow, Ui_WeatherWindow
import sys, config
import requests

app = QApplication(sys.argv)

MainWindow = QWidget()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

def get_city():
    res = requests.get("http://ip-api.com/json?fields=country,city",
                       params={"lang": config.language}
                       )
    data = res.json()
    return data['city']

def get_coords(city):
    if config.language == "ru":
      lang = "ru_RU"
    else:
      lang = "en_US"
    res = requests.get("https://geocode-maps.yandex.ru/1.x",
                       params={"geocode": city,
                               "apikey": config.GeocoderAPIKey,
                               "sco": "latlong",
                               "format": "json",
                               "results": "1",
                               "lang": lang}
                       )
    if not res.status_code == 200:
      if config.language == "ru":
        error("Неправильный API ключ Яндекс.Геокодера")
      else:
        error("Wrong API key for Yandex.Geocoder")
    else:
      data = res.json()
      coords = ((((((data["response"])["GeoObjectCollection"])["featureMember"])[0])["GeoObject"])["Point"])["pos"].partition(" ")
      coords = {"lat": coords[2], "lon": coords[0]}
      return coords

def get_weather(lat, lon):
    if config.language == "ru":
      lang = "ru_RU"
    else:
      lang = "en_US"
    res = requests.get("https://api.weather.yandex.ru/v1/forecast/",
                       params={"lat": lat, "lon": lon,
                               "lang": lang, "limit": 1},
                       headers={"X-Yandex-API-Key": config.WeatherAPIKey}
                       )
    if not res.status_code == 200:
      if config.language == "ru":
        error("Неправильный API ключ Яндекс.Погоды")
      else:
        error("Wrong API key for Yandex.Weathers")
    else:
        data = res.json()
        weather = data["fact"]
        #Traslate
        if config.language == "ru":
          if weather["condition"] == "clear":
            weather["condition"] = "Ясно"
          elif weather["condition"] == "cloudy":
            weather["condition"] = "Облачно с прояснениями"
          elif weather["condition"] == "overcast":
            weather["condition"] = "Пасмурно"
          elif weather["condition"] == "partly-cloudy":
            weather["condition"] = "Малооблачно"
          elif (weather["condition"] == "partly-cloudy-and-light-rain") or (weather["condition"] == "cloudy-and-light-rain") or (weather["condition"] == "overcast-and-light-rain"):
            weather["condition"] = "Небольшой дождь"
          elif (weather["condition"] == "partly-cloudy-and-rain") or (weather["condition"] == "cloudy-and-rain"):
            weather["condition"] = "Дождь"
          elif weather["condition"] == "overcast-and-rain":
            weather["condition"] = "Сильный дождь"
          elif weather["condition"] == "overcast-thunderstorms-with-rain":
            weather["condition"] = "Сильный дождь, гроза"
          elif weather["condition"] == "overcast-and-wet-snow":
            weather["condition"] = "Дождь со снегом"
          elif weather["condition"] == "partly-cloudy-and-light-snow":
            weather["condition"] = "Небольшой снег"
          elif weather["condition"] == "partly-cloudy-and-snow":
            weather["condition"] = "Снег"
          return weather
        else:
          return weather

def error(text):
    mbox = QMessageBox()

    if config.language == "ru":
      windowname = "Ошибка"
    else:
      windowname = "Error"

    mbox.setWindowTitle(windowname)
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
        if config.language == "ru":
          uiw.templbl.setText(str(weather["temp"]) + "°С")
          uiw.feelslbl.setText("Ощущается как: " + str(weather["feels_like"]) + "°С")
          uiw.windspeed.setText("Скорость ветра: " + str(weather["wind_speed"]) + " м/с")
          uiw.airhumidity.setText("Влажность: " + str(weather["humidity"]) + " %")
          uiw.pressure.setText("Давление: " + str(weather["pressure_mm"]) + " мм рт. ст.")
        else:
          uiw.templbl.setText(str(weather["temp"]) + "°С")
          uiw.feelslbl.setText("Feels like: " + str(weather["feels_like"]) + "°С")
          uiw.windspeed.setText("Wind speed: " + str(weather["wind_speed"]) + " m/s")
          uiw.airhumidity.setText("Air humidity: " + str(weather["humidity"]) + " %")
          uiw.pressure.setText("Pressure: " + str(weather["pressure_mm"]) + " mm Hg.")

        WeatherWindow.show()
        WeatherWindow.exec()
    except IndexError:
      if config.language == "ru":
        error("Неправильно введён город или нет подключения к Интернету")
      else:
        error("The city was entered incorrectly or there is no Internet connection")

ui.wbtn.clicked.connect(auto_city)
ui.wbtnr.clicked.connect(weather)

sys.exit(app.exec_())
