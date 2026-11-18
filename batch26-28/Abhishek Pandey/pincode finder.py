
import urllib.request
import json

print("==============================")
print("      📮 PIN CODE FINDER")
print("==============================")

pincode = input("Enter 6-digit PIN code: ").strip()

if len(pincode) != 6 or not pincode.isdigit():
    print("❌ Please enter a valid 6-digit PIN code.")
    exit()

url = "https://api.postalpincode.in/pincode/" + pincode

try:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    response = urllib.request.urlopen(request, timeout=10)

    data = json.loads(response.read().decode("utf-8"))

    result = data[0]

    if result["Status"] == "Success":

        offices = result["PostOffice"]

        print("\n==============================")
        print("      PIN CODE INFORMATION")
        print("==============================")

        print("PIN Code :", pincode)
        print("District :", offices[0]["District"])
        print("State    :", offices[0]["State"])
        print("Country  :", offices[0]["Country"])

        print("\nPost Offices:")

        for office in offices:
            print("-", office["Name"])

        print("==============================")

    else:
        print("\n❌ PIN code not found.")

except Exception as e:
    print("\n❌ Error:")
    print(e)
