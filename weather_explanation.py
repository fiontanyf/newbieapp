import requests

endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "London,UK", "units":"metric", "appid":"YOUR_APP_ID"}
#the key is london, units are metric and appid is a password.

#if we try to get q out we can get out London 

response = requests.get(endpoint, params=payload)
data = response.json()

print (response.url)
print (response.status_code)
print (response.headers["content-type"])
print (response.text)

temperature = data["main"]["temp"]
name = data["name"]
weather = data["weather"][0]["main"]
print u"It's {}C in {}, and the sky is {}".format(temperature, name, weather)