import requests

municipality = input("Enter municipality name: ")

request1 = f"http://api.openweathermap.org/geo/1.0/direct?q={municipality}&appid=b95a6514910ba7e094857266b4391fe4"
respond1 = requests.get(request1).json()

lat, lon = respond1[0]["lat"], respond1[0]["lon"]

request2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=b95a6514910ba7e094857266b4391fe4"

try:
    respond2 = requests.get(request2)

    if respond2.status_code == 200:
        print(f"Weather: {respond2.json()["weather"][0]["description"]}\nTemperature: {round(respond2.json()["main"]["temp"] - 273, 1)} Celsius")

except Exception as e:
    print(e)