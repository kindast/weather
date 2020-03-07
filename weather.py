import requests

def get_city():
    res = requests.get("http://ip-api.com/json?fields=country,city",
                       params={'lang': 'ru'}
                       )
    data = res.json()
    return data['city']

def get_coords(city):
    res = requests.get("http://www.datasciencetoolkit.org/maps/api/geocode/json",
                       params={'address': city}
                       )
    data = res.json()
    data = data['results']
    data = data[0]
    data = data["geometry"]
    data = data["location"]
    coords = {'lat': data['lat'], 'lon': data['lng']}
    return coords

def get_weather(lat, lon):
    YandexAPIkey = 'b077e320-1ebd-4074-816d-37f6a7ae9bb9'
    res = requests.get("https://api.weather.yandex.ru/v1/forecast/",
                       params={'lat': lat, 'lon': lon, 'lang': 'ru_RU', 'limit': 1},
                       headers={'X-Yandex-API-Key': YandexAPIkey}
                       )
    data = res.json()
    return data['fact']

def print_weather(weather, city):
    if weather['condition'] == "clear":
        weather['condition'] = "ясно"
    elif weather['condition'] == "cloudy":
        weather['condition'] = "облачно с прояснениями"
    elif weather['condition'] == "overcast":
        weather['condition'] = "пасмурно"
    elif weather['condition'] == "partly-cloudy":
        weather['condition'] = "малооблачно"
    elif weather['condition'] == "partly-cloudy-and-light-rain":
        weather['condition'] = "небольшой дождь"
    elif weather['condition'] == "partly-cloudy-and-rain":
        weather['condition'] = "дождь"
    elif weather['condition'] == "overcast-and-rain":
        weather['condition'] = "сильный дождь"
    elif weather['condition'] == "overcast-thunderstorms-with-rain":
        weather['condition'] = "сильный дождь, гроза"
    elif (weather['condition'] == "cloudy-and-light-rain") or (weather['condition'] == "overcast-and-light-rain"):
        weather['condition'] = "небольшой дождь"
    elif weather['condition'] == "cloudy-and-rain":
        weather['condition'] = "дождь"
    elif weather['condition'] == "overcast-and-wet-snow":
        weather['condition'] = "дождь со снегом"
    elif weather['condition'] == "partly-cloudy-and-light-snow":
        weather['condition'] = "небольшой снег"
    elif weather['condition'] == "partly-cloudy-and-snow":
        weather['condition'] = "снег"
    elif weather['condition'] == "overcast-and-wet-snow":
        weather['condition'] = "дождь со снегом"
    print("По данным Яндекс.Погоды в городе " + city, "сейчас:")
    print("Погода:",weather['condition'])
    print("Температура:",weather['temp'],"градусов Цельсия")
    print("Ощущается как:",weather['feels_like'],"градусов Цельсия")
    print("Скорость ветра:",weather['wind_speed'],"м/с")
    print("Влажность воздуха:",weather['humidity'],"%")

while True:
    print('[0] Выход из программы')
    print('[1] Узнать погоду')
    user_input = int(input(": "))
    if user_input == 0:
        break
    if user_input == 1:
        print('[1] Автоматическое определение местоположения (Не всегда точное)')
        print('[2] Ручной ввод')
        user_input2 = int(input(": "))
        if user_input2 == 1:
            city = get_city()
            coords = get_coords(city)
            weather = get_weather(coords['lat'], coords['lon'])
            print_weather(weather, city)
        if user_input2 == 2:
            city = str(input("Город: "))
            coords = get_coords(city)
            weather = get_weather(coords['lat'], coords['lon'])
            print_weather(weather, city)
            
        
