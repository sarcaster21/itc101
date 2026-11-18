import urllib.request
import json

print("==============================")
print("       ADVICE GENERATOR")
print("==============================")

url = "https://api.adviceslip.com/advice"

try:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    response = urllib.request.urlopen(request, timeout=10)

    data = json.loads(response.read().decode("utf-8"))

    advice = data["slip"]["advice"]

    print("\n💡 Random Advice:")
    print("------------------------------")
    print(advice)
    print("------------------------------")

except Exception as e:
    print("\n❌ Error occurred:")
    print(e)