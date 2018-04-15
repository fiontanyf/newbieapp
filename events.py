import requests

url = "https://www.eventbriteapi.com/v3/events/search/?location.address=London&token=NSPHS3E5DNMF4YU4BCW4"


response = requests.get(url) #, params=payload)
data = response.json()

print (response.url)
print (response.status_code)
print (response.headers["content-type"])
print (response.text)

# key 
# BIKI4SWWUFIIDNNN6O