import urllib.request
import json

print("==============================")
print("       GITHUB USER FINDER")
print("==============================")

username = input("Enter GitHub username: ")

url = "https://api.github.com/users/" + username

try:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Python"}
    )

    response = urllib.request.urlopen(request)
    data = json.loads(response.read())

    print("\n------------------------------")
    print("Name        :", data["name"])
    print("Username    :", data["login"])
    print("Repositories:", data["public_repos"])
    print("Followers   :", data["followers"])
    print("Following   :", data["following"])
    print("Profile     :", data["html_url"])
    print("------------------------------")

except Exception:
    print("\n❌ GitHub user not found.")