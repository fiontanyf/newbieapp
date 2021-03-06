import requests

endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "London,UK", "units":"metric", "appid":"7c342186dbca07aef649cd07af2b77f1"}

response = requests.get(endpoint, params=payload)
data = response.json()

print response.url
print response.status_code
print response.headers["content-type"]
print response.text


temperature = data["main"]["temp"]
name = data["name"]
weather = data["weather"][0]["main"]
print u"It's {}C in {}, and the sky is {}".format(temperature, name, weather)