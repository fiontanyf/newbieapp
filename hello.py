from flask import Flask, render_template, request

app=Flask("MyApp") # defining a flas application with the name my app

@app.route("/events") #decorator- very powerful in python ,  #when user calls e.g. bbc.co.uk/
def eventslist():
	return " events page!"
	return render_template("eventstext.html", name=name.title())


import requests

url = "https://www.eventbriteapi.com/v3/events/search/?sort_by=distance&location.address=London&location.within=1mi&token=NSPHS3E5DNMF4YU4BCW4"


response = requests.get(url) #, params=payload)
data = response.json()

print (response.url)
print (response.status_code)
print (response.headers["content-type"])
print (response.text)

#test
# key 
# BIKI4SWWUFIIDNNN6O

#when we put a /X in our url, we get hello X displayed on the page. that X is stored as a 
#variable called name.



app.run(debug=True) # this allows us to run the application 