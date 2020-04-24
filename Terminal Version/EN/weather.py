import requests, config

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
      print("Wrong API key for Yandex.Geocoder")
      return True
    else:
      data = res.json()
      coords = ((((((data["response"])["GeoObjectCollection"])["featureMember"])[0])["GeoObject"])["Point"])["pos"].partition(" ")
      coords = {"lat": coords[2], "lon": coords[0]}
      return coords

def get_weather(lat, lon):
    res = requests.get("https://api.weather.yandex.ru/v1/forecast/",
                       params={"lat": lat, "lon": lon, "lang": "en_US", "limit": 1},
                       headers={"X-Yandex-API-Key": config.WeatherAPIKey}
                       )
    if not res.status_code == 200:
      print("Wrong API key for Yandex.Weathers")
      return True
    else:
      data = res.json()
      return data["fact"]

def print_weather(weather, city):
    print("According to Yandex.Weather in the city " + city + ":\n"
          "Weather:",weather['condition'] + "\n"
          "Temperature:",weather['temp'],"degrees Celsius", "|" " Feels like:",weather['feels_like'],"degrees Celsius" + "\n"
          "Wind speed:",weather['wind_speed'],"m/s" + "\n"
          "Air humidity:",weather['humidity'],"%" + "\n"
          "Pressure:",weather["pressure_mm"],"mm Hg." + "\n")

while True:
 try:
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
               city = str(input("City: "))
               coords = get_coords(city)
               if coords == True:
                break
               print("\nGetting weather information ...\n")
               weather = get_weather(coords["lat"], coords["lon"])
               if weather == True:
                break
               print_weather(weather, city)
     except IndexError:
            print("City name entered incorrectly")
        
     if user_input == 2:
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
    print("No internet connection")
