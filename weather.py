import requests
import customtkinter as ct
from tkinter import messagebox

ct.set_appearance_mode("light")

root = ct.CTk()
root.geometry('400x400')
root.title("Pol's Weather App")


def show_weather(city):
    try:
        api_key = open("API_key", "r").read()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url).json()
        temperature_kelvin = response["main"]["temp"]
        humidity = response["main"]["humidity"]
        wind_speed = response["wind"]["speed"]
        temperature_celsius = temperature_kelvin - 273.15
        weather_info = (f"City: {city}\nTemperature: {temperature_celsius:.2f}°C\nHumidity: {humidity}%\n"
                        f"Wind Speed: {wind_speed} m/s")
        messagebox.showinfo("Weather Info", weather_info)
    except Exception as e:
        messagebox.showerror("Error", "Failed to retrieve weather data.")


def load_cities(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()


def city_buttons(cities):
    row = 0
    for city in cities:
        button = ct.CTkButton(master=root, text=city, command=lambda c=city: show_weather(c), corner_radius=10,
                              width=150, height=40)
        button.grid(row=row, column=0, padx=10, pady=5)
        row += 1


cities = load_cities("cities.txt")
city_buttons(cities)

root.mainloop()
