import requests

request = "https://api.chucknorris.io/jokes/random"

try:
    respond = requests.get(request)

    if respond.status_code == 200:
        print(respond.json()["value"])

except Exception as e:
    print(e)
