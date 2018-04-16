from flask import Flask, render_template, jsonify, request
import requests
from key import key
import imghdr
import os

app = Flask(__name__)
# app = Flask('MapApp')
port = int(os.environ.get("PORT", 5000))

search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
photos_url = "https://maps.googleapis.com/maps/api/place/photo"

# HIDE KEY 
# config_file = 'config.json'
# # The check below is to see if you have the
# # config file defined and if you do not, it will display
# # basic guidelines steps to set the config file.
# if not os.path.isfile(config_file):
#     app.logger.error(
#         "Your config.json file is missing." +
#         "You need to create one in order for this demo app to run." +
#         "Please check the README.md file in order to set it up."
#     )
# else:
#     # We are in the case where we have the config file.
#     #
#     # The line below is the magic statement that is going
#     # to load our configuration from the config.json file.
#     # After the line below is executed the config defined
#     # in config.json will be available in the app variable.
#     # Example on how you can get the config values:
#     # secret_key = app.secret_key
#     # OR
#     # secret_key = app.config['SECRET_KEY']
#     app.config.from_json(config_file)
#
# @app.route('/my_key')
# def my_key():
#     my_config_secret_key = app.config['key']
#
#     if my_config_secret_key:
#         app.logger.debug("Your secret key is: " + my_config_secret_key)
#     else:
#         app.logger.debug("No SECRET_KEY defined in the config.json")
#
#     return "You should see your secret key in the terminal output"






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

    event_data = get_events(query)
    print event_data

    return '<img src='+ photo_name + '>'


# greeting message
@app.route("/location" , methods=["POST"])
def name():
    form_data = request.form
    print "HELLO"
    name = form_data["name"]
    return render_template('location.html', name=name )







if __name__ ==  "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)
    # app.run(debug=True)
