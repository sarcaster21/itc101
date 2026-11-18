import urllib.request
import json

print("==============================")
print("      CURRENCY CONVERTER")
print("==============================")

amount = float(input("Enter amount in USD: "))

url = "https://open.er-api.com/v6/latest/USD"

try:
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    rate = data["rates"]["INR"]
    result = amount * rate

    print("\n------------------------------")
    print("USD Amount    :", amount)
    print("1 USD = INR   :", rate)
    print("INR Amount    :", round(result, 2))
    print("------------------------------")

except Exception as e:
    print("Something went wrong.")
    print("Error:", e)

