# 1a5bfc796e1d4aa6960221503253108 
import requests

city = "London"
url = "http://api.weatherapi.com/v1/current.json?key=1a5bfc796e1d4aa6960221503253108&q="+city+"&aqi=no"
response = requests.get(url)
weather_json = response.json()
# print(weather_json)

temperature_f = weather_json.get("current").get("temp_f")
# print(f"The current temperature in Miami is {temperature_f}°F")
description = weather_json.get("current").get("condition").get("text")
print(f"Today's weather in {city} is {temperature_f} and {description}")

