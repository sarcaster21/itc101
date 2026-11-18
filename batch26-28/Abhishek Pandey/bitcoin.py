import urllib.request
import json

print("==============================")
print("       BITCOIN PRICE")
print("==============================")

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

try:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    response = urllib.request.urlopen(request, timeout=10)

    data = json.loads(response.read().decode("utf-8"))

    price = data["bitcoin"]["usd"]

    print()
    print("Bitcoin Price")
    print("------------------------------")
    print("BTC = $", price)
    print("------------------------------")

except Exception as e:
    print()
    print("ERROR:")
    print(e)