import requests

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
                       params={"lat": lat, "lon": lon, "lang": "en_US", "limit": 1},
                       headers={"X-Yandex-API-Key": YandexAPIkey}
                       )
    data = res.json()
    return data["fact"]

def print_weather(weather, city):
    print("According to Yandex.Weather in the city " + city + ":")
    print("Weather:",weather['condition'])
    print("Temperature:",weather['temp'],"degrees Celsius", "|" " Feels like:",weather['feels_like'],"degrees Celsius")
    print("Wind speed:",weather['wind_speed'],"m/s")
    print("Air humidity:",weather['humidity'],"%")
    print("Pressure:",weather["pressure_mm"],"mm Hg. Art.")
    print(" ")

while True:
 try:
     print("[2] Auto Location")
     print("[1] Manual input")
     print("[0] Exit from the program")
     user_input = int(input(": "))
     if user_input == 0:
         break
     try:
           if user_input == 1:
               print(" ")
               city = str(input("City: "))
               coords = get_coords(city)
               print(" ")
               print("Getting weather information ...")
               print(" ")
               weather = get_weather(coords["lat"], coords["lon"])
               print_weather(weather, city)
     except:
            print("No internet connection or city name entered incorrectly")
        
     if user_input == 2:
         print(" ")
         print("Getting weather information for your location ...")
         print(" ")
         city = get_city()
         coords = get_coords(city)
         weather = get_weather(coords["lat"], coords["lon"])
         print_weather(weather, city)
 except:
    print("No internet connection")
