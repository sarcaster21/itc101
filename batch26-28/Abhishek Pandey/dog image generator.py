import urllib.request
import json
import webbrowser

print("==============================")
print("      🐶 RANDOM DOG")
print("==============================")

url = "https://dog.ceo/api/breeds/image/random"

try:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    response = urllib.request.urlopen(request, timeout=10)

    data = json.loads(response.read().decode("utf-8"))

    image_url = data["message"]

    print("\n🐶 Random Dog Image:")
    print(image_url)

    # Open the dog image in your browser
    webbrowser.open(image_url)

except Exception as e:
    print("\n❌ Error occurred:")
    print(e)