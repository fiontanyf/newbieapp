from flask import Flask, render_template, jsonify, request
import requests
from key import key
import imghdr
import os

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
photos_url = "https://maps.googleapis.com/maps/api/place/photo"

@app.route("/", methods=["GET"])
def retreive():
    return render_template('homepage.html')

@app.route("/sendRequest/<string:query>")

def results(query):
    strip_query = query.replace(" ", "")
    search_payload = {"key":key, "query":strip_query}
    search_req = requests.get(search_url, params=search_payload)
    search_json = search_req.json()

    photo_id = search_json["results"][0]["photos"][0]["photo_reference"]

    photo_payload = {"key" : key, "maxwidth" : 500, "maxwidth" : 500, "photoreference" : photo_id}
    photo_request = requests.get(photos_url, params=photo_payload)

    photo_type = imghdr.what("", photo_request.content)
    photo_name = "static/" + strip_query + "." + photo_type

    with open(photo_name, "wb") as photo:
        photo.write(photo_request.content)

    return '<img src='+ photo_name + '>'


# greeting message
@app.route("/location" , methods=["POST"])
def name():
    form_data = request.form
    name = form_data["name"]
    return render_template('location.html', name=name )


if __name__ ==  "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=port, debug=True)
