import urllib.request
import json
from datetime import datetime

print("==============================")
print("     🌍 EARTHQUAKE TRACKER")
print("==============================")

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"

try:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    response = urllib.request.urlopen(request, timeout=15)

    data = json.loads(response.read().decode("utf-8"))

    earthquakes = data["features"]

    print("\nTotal earthquakes today:", len(earthquakes))
    print("\nLatest Earthquakes")
    print("------------------------------")

    for earthquake in earthquakes[:10]:

        properties = earthquake["properties"]

        place = properties["place"]
        magnitude = properties["mag"]
        time = properties["time"]

        date_time = datetime.fromtimestamp(time / 1000)

        print("\nLocation   :", place)
        print("Magnitude  :", magnitude)
        print("Time       :", date_time)
        print("------------------------------")

except Exception as e:
    print("\n❌ ERROR")
    print(e)