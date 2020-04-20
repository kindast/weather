import requests

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
    coords = {"lat": coords[2], "lon": coords[0]}
    return coords

def get_weather(lat, lon):
    YandexAPIkey = "0c0ec0c2-2aeb-4710-9e72-be9f4127ad6f"
    res = requests.get("https://api.weather.yandex.ru/v1/forecast/",
                       params={"lat": lat, "lon": lon, "lang": "ru_RU", "limit": 1},
                       headers={"X-Yandex-API-Key": YandexAPIkey}
                       )
    data = res.json()
    return data["fact"]

def print_weather(weather, city):
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

while True:
 try:
     print("=============================================\n"
           "[2] Автоматическое определение местоположения\n"
           "[1] Ручной ввод\n"
           "[0] Выход из программы\n"
           "=============================================")
     user_input = int(input(": "))
     if user_input == 0:
         break
     try:
           if user_input == 1:
               city = str(input("Город: "))
               coords = get_coords(city)
               print("\nПолучение информации о погоде ...\n")
               weather = get_weather(coords["lat"], coords["lon"])
               print_weather(weather, city)
     except:
            print("Нет подключения к Интернету или название города введено неправильно")
        
     if user_input == 2:
         print("\nПолучение информации о погоде для вашего местоположения ...\n")
         city = get_city()
         coords = get_coords(city)
         weather = get_weather(coords["lat"], coords["lon"])
         print_weather(weather, city)
 except:
    print("Нет подключения к Интернету")
