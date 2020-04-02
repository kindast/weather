import requests

def get_city():
    res = requests.get("http://ip-api.com/json?fields=country,city",
                       params={"lang": "ru"}
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
    elif weather["condition"] == "partly-cloudy-and-light-rain":
        weather["condition"] = "небольшой дождь"
    elif weather["condition"] == "partly-cloudy-and-rain":
        weather["condition"] = "дождь"
    elif weather["condition"] == "overcast-and-rain":
        weather["condition"] = "сильный дождь"
    elif weather["condition"] == "overcast-thunderstorms-with-rain":
        weather["condition"] = "сильный дождь, гроза"
    elif (weather["condition"] == "cloudy-and-light-rain") or (weather["condition"] == "overcast-and-light-rain"):
        weather["condition"] = "небольшой дождь"
    elif weather["condition"] == "cloudy-and-rain":
        weather["condition"] = "дождь"
    elif weather["condition"] == "overcast-and-wet-snow":
        weather["condition"] = "дождь со снегом"
    elif weather["condition"] == "partly-cloudy-and-light-snow":
        weather["condition"] = "небольшой снег"
    elif weather["condition"] == "partly-cloudy-and-snow":
        weather["condition"] = "снег"
    elif weather["condition"] == "overcast-and-wet-snow":
        weather["condition"] = "дождь со снегом"
    print("По данным Яндекс.Погоды в городе " + city + ":")
    print("Погода:",weather['condition'])
    print("Температура:",weather['temp'],"градусов Цельсия", "|" " Ощущается как:",weather['feels_like'],"градусов Цельсия")
    print("Скорость ветра:",weather['wind_speed'],"м/с")
    print("Влажность воздуха:",weather['humidity'],"%")
    print("Давление:",weather["pressure_mm"],"мм рт. ст.")
    print(" ")

while True:
 try:
     print("[2] Автоматическое определение местоположения")
     print("[1] Ручной ввод")
     print("[0] Выход из программы")
     user_input = int(input(": "))
     if user_input == 0:
         break
     try:
           if user_input == 1:
               print(" ")
               city = str(input("Город: "))
               coords = get_coords(city)
               print(" ")
               print("Получение информации о погоде ...")
               print(" ")
               weather = get_weather(coords["lat"], coords["lon"])
               print_weather(weather, city)
     except:
            print("Нет подключения к Интернету или название города введено неправильно")
        
     if user_input == 2:
         print(" ")
         print("Получение информации о погоде для вашего местоположения ...")
         print(" ")
         city = get_city()
         coords = get_coords(city)
         weather = get_weather(coords["lat"], coords["lon"])
         print_weather(weather, city)
 except:
    print("Нет подключения к Интернету")
