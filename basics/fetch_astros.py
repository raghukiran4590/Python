import requests

response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()
# print(data)

print("The people currently in space are :")
for person in data["people"]:
    print(person["name"])

