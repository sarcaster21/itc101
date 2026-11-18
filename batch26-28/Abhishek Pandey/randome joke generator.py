import urllib.request
import json

url = "https://official-joke-api.appspot.com/random_joke"

try:
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    print("\n😂 RANDOM JOKE")
    print("-----------------------")
    print(data["setup"])
    print(data["punchline"])

except Exception as e:
    print("Error:", e)