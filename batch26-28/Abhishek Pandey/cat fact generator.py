import urllib.request
import json

print("==============================")
print("      🐱 CAT FACT GENERATOR")
print("==============================")

url = "https://catfact.ninja/fact"

try:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    response = urllib.request.urlopen(request, timeout=10)

    data = json.loads(response.read().decode("utf-8"))

    print("\n🐱 Random Cat Fact:")
    print(data["fact"])

except Exception as e:
    print("\n❌ Error occurred:")
    print(e)