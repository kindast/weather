from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *
from ui import MainUI, WeatherUI, SettingsUI
import sys, requests

#Config
config = open("config.txt", mode="r")
text = config.read()
weatherAPI = text.partition('"')[2].partition('"')[0]
geocoderAPI = text.partition('"')[2].partition('"')[2].partition('"')[2].partition('"')[0]
language = text.partition('"')[2].partition('"')[2].partition('"')[2].partition('"')[2].partition('"')[2].partition('"')[0]
config.close()

#Create Application
app = QApplication(sys.argv)

#Main
MainWindow = QWidget()
ui = MainUI()
ui.setupMainUI(MainWindow)
MainWindow.show()

#Settings
SettingsWindow = QWidget()
uis = SettingsUI()
uis.setupSettingsUI(SettingsWindow)

#Weather
WeatherWindow = QWidget()
uiw = WeatherUI()
uiw.setupWeatherUI(WeatherWindow)

#Functions
def get_city():
    res = requests.get("http://ip-api.com/json?fields=country,city",
                       params={"lang": language}
                       )
    data = res.json()
    return data['city']

def get_coords(city):
    if language == "ru":
      lang = "ru_RU"
    else:
      lang = "en_US"
    res = requests.get("https://geocode-maps.yandex.ru/1.x",
                       params={"geocode": city,
                               "apikey": geocoderAPI,
                               "sco": "latlong",
                               "format": "json",
                               "results": "1",
                               "lang": lang}
                       )
    if not res.status_code == 200:
      if language == "ru":
        error("Неправильный API ключ Яндекс.Геокодера")
      else:
        error("Wrong API key for Yandex.Geocoder")
    else:
      data = res.json()
      coords = ((((((data["response"])["GeoObjectCollection"])["featureMember"])[0])["GeoObject"])["Point"])["pos"].partition(" ")
      coords = {"lat": coords[2], "lon": coords[0]}
      return coords

def get_weather(lat, lon):
    if language == "ru":
      lang = "ru_RU"
    else:
      lang = "en_US"
    res = requests.get("https://api.weather.yandex.ru/v1/forecast/",
                       params={"lat": lat, "lon": lon,
                               "lang": lang, "limit": 1},
                       headers={"X-Yandex-API-Key": weatherAPI}
                       )
    if not res.status_code == 200:
      if language == "ru":
        error("Неправильный API ключ Яндекс.Погоды")
      else:
        error("Wrong API key for Yandex.Weathers")
    else:
        data = res.json()
        weather = data["fact"]
        #Traslate
        if language == "ru":
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

    if language == "ru":
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

def save():
    config = open("config.txt", mode="w")
    wapi = 'weatherAPI = "' + uis.apiweather.text() + '"'
    gapi = 'geocoderAPI = "' + uis.apigeocoder.text() + '"'
    if uis.langbox.currentText() == "Русский":
      lang = 'language = "ru"'
    else:
      lang = 'language = "en"'
    config.write(wapi + "\n" + gapi + "\n" + lang)
    config.close()
    if language == "ru":
      error("Перезагрузи программу")
    else:
      error("Restart the program")

def settings():
    SettingsWindow.show()

    uis.apiweather.setText(weatherAPI)
    uis.apigeocoder.setText(geocoderAPI)
    #Icon USA
    icon = QIcon()
    icon.addFile(u"icons/usa.png", QSize(), QIcon.Normal, QIcon.Off)
    #Icon Russia
    icon1 = QIcon()
    icon1.addFile(u"icons/russia.png", QSize(), QIcon.Normal, QIcon.Off)
    if language == "ru":
      uis.langbox.addItem(icon1, "Русский")
      uis.langbox.addItem(icon, "English")
    else:
      uis.langbox.addItem(icon, "English")
      uis.langbox.addItem(icon1, "Русский")

    SettingsWindow.exec()

def auto_city(self):
    city = get_city()
    ui.lineedit.setText(city)

def weather(self):
    try:
        city = ui.lineedit.text()
        coords = get_coords(city)
        weather = get_weather(coords["lat"], coords["lon"])

        WeatherWindow.setWindowTitle(city)
        uiw.citylbl.setText(city)
        uiw.weatherlbl.setText(weather["condition"])
        if language == "ru":
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
      if language == "ru":
        error("Неправильно введён город или нет подключения к Интернету")
      else:
        error("The city was entered incorrectly or there is no Internet connection")

#Buttons
ui.wbtn.clicked.connect(auto_city)
ui.wbtnr.clicked.connect(weather)
ui.setbtn.clicked.connect(settings)
uis.savebtn.clicked.connect(save)

sys.exit(app.exec_())
