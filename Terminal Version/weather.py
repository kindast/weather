import requests, config

print("Выберите язык/Choose the language:\n"
      "[0] Русский\n"
      "[1] English")
choice = int(input(": "))
if choice == 0:
  language = ["ru", "ru_RU"]
else:
  language = ["en", "en_US"]

def get_city():
    res = requests.get("http://ip-api.com/json?fields=country,city",
                       params={"lang": language[0]}
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
                               "lang": language[1]}
                       )
    if not res.status_code == 200:
      if language[0] == "ru":
        print("Неправильный API ключ Яндекс.Геокодера")
      else:
        print("Wrong API key for Yandex.Geocoder")
      return True
    else:
      data = res.json()
      coords = ((((((data["response"])["GeoObjectCollection"])["featureMember"])[0])["GeoObject"])["Point"])["pos"].partition(" ")
      coords = {"lat": coords[2], "lon": coords[0]}
      return coords

def get_weather(lat, lon):
    res = requests.get("https://api.weather.yandex.ru/v1/forecast/",
                       params={"lat": lat, "lon": lon, "lang": language[1], "limit": 1},
                       headers={"X-Yandex-API-Key": config.WeatherAPIKey}
                       )
    if not res.status_code == 200:
      if language[0] == "ru":
        print("Неправильный API ключ Яндекс.Погоды")
      else:
        print("Wrong API key for Yandex.Weathers")
      return True
    else:
      data = res.json()
      return data["fact"]

def print_weather(weather, city):
    if language[0] == "ru":
      if weather["condition"] == "clear":
        weather["condition"] = "ясно"
      elif weather["condition"] == "cloudy":
        weather["condition"] = "облачно с прояснениями"
      elif weather["condition"] == "overcast":
        weather["condition"] = "пасмурно"
      elif weather["condition"] == "partly-cloudy":
        weather["condition"] = "малооблачно"
      elif (weather["condition"] == "partly-cloudy-and-light-rain") or (weather["condition"] == "cloudy-and-light-rain") or (weather["condition"] == "overcast-and-light-rain"):
        weather["condition"] = "небольшой дождь"
      elif (weather["condition"] == "partly-cloudy-and-rain") or (weather["condition"] == "cloudy-and-rain"):
        weather["condition"] = "дождь"
      elif weather["condition"] == "overcast-and-rain":
        weather["condition"] = "сильный дождь"
      elif weather["condition"] == "overcast-thunderstorms-with-rain":
        weather["condition"] = "сильный дождь, гроза"
      elif weather["condition"] == "overcast-and-wet-snow":
        weather["condition"] = "дождь со снегом"
      elif weather["condition"] == "partly-cloudy-and-light-snow":
        weather["condition"] = "небольшой снег"
      elif weather["condition"] == "partly-cloudy-and-snow":
        weather["condition"] = "снег"
      print("По данным Яндекс.Погоды в городе " + city + ":" + "\n" 
          "Погода:",weather['condition'] + "\n"
          "Температура:",weather['temp'],"градусов Цельсия", "|" " Ощущается как:",weather['feels_like'],"градусов Цельсия" + "\n"
          "Скорость ветра:",weather['wind_speed'],"м/с" + "\n"
          "Влажность воздуха:",weather['humidity'],"%" + "\n"
          "Давление:",weather["pressure_mm"],"мм рт. ст." + "\n")
    else:
      print("According to Yandex.Weather in the city " + city + ":\n"
          "Weather:",weather['condition'] + "\n"
          "Temperature:",weather['temp'],"degrees Celsius", "|" " Feels like:",weather['feels_like'],"degrees Celsius" + "\n"
          "Wind speed:",weather['wind_speed'],"m/s" + "\n"
          "Air humidity:",weather['humidity'],"%" + "\n"
          "Pressure:",weather["pressure_mm"],"mm Hg." + "\n")

while True:
  try:
     if language[0] == "ru":
       print("=============================================\n"
             "[2] Автоматическое определение местоположения\n"
             "[1] Ручной ввод\n"
             "[0] Выход из программы\n"
             "=============================================")
     else:
       print("=========================\n"
             "[2] Auto Location\n"
             "[1] Manual input\n"
             "[0] Exit from the program\n"
             "=========================")
     user_input = int(input(": "))
     if user_input == 0:
         break
     try:
           if user_input == 1:
               if language[0] == "ru":
                 city = str(input("Город: "))
                 print("\nПолучение информации о погоде ...\n")
               else:
                 city = str(input("City: "))
                 print("\nGetting weather information ...\n")
               coords = get_coords(city)
               if coords == True:
                break
               weather = get_weather(coords["lat"], coords["lon"])
               if weather == True:
                break
               print_weather(weather, city)
     except IndexError:
            if language[0] == "ru":
              print("Название города введено неправильно")
            else:
              print("City name entered incorrectly")
        
     if user_input == 2:
         if language[0] == "ru":
           print("\nПолучение информации о погоде для вашего местоположения ...\n")
         else:
           print("\nGetting weather information for your location ...\n")
         city = get_city()
         coords = get_coords(city)
         if coords == True:
          break
         weather = get_weather(coords["lat"], coords["lon"])
         if weather == True:
          break
         print_weather(weather, city)
  except:
    if language[0] == "ru":
      print("Нет подключения к Интернету")
    else:
      print("No internet connection")
