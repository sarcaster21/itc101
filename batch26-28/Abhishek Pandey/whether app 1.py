import urllib.request
import json

city = input("Enter city name: ")

url = "https://wttr.in/" + city + "?format=j1"

try:
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    weather = data["current_condition"][0]

    print("\n==============================")
    print("       WEATHER SYSTEM")
    print("==============================")
    print("City        :", city)
    print("Temperature :", weather["temp_C"], "°C")
    print("Feels Like  :", weather["FeelsLikeC"], "°C")
    print("Humidity    :", weather["humidity"], "%")
    print("Wind Speed  :", weather["windspeedKmph"], "km/h")
    print("Condition   :", weather["weatherDesc"][0]["value"])
    print("==============================")

except Exception as e:
    print("Something went wrong.")
    print("Error:", e)
