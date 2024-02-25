import requests
import datetime as dt

URL = "https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=d9c932d13b5d646848aae3328f94c9f5"

api = open("API_key", "r").read()
city = "Brisbane,au"
city_index = "&APPID="
weather = "https://api.openweathermap.org/data/2.5/weather"

request_weather = weather + "?q=" + city + city_index + api

response = requests.get(request_weather).json()
temperature_kelvin = response["main"]["temp"]
humidity = response["main"]["humidity"]
wind_speed = response["wind"]["speed"]

print(f"Влажность: {humidity}%")
print(f"Скорость ветра: {wind_speed} м/c")


def kelvin_to_celsius(kelvin):
    celcsius = kelvin - 273.15
    return celcsius


print(kelvin_to_celsius(temperature_kelvin))


def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9 / 5 + 32
    return fahrenheit


print(f"Температура: {kelvin_to_fahrenheit(temperature_kelvin):.2f}°F")

