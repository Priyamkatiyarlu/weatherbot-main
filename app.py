from flask import Flask,request,jsonify
import requests
import urllib.request
import json
app=Flask(__name__)

@app.route('/',methods=["POST","GET"])
def index():
    data=request.get_json()
    city=data['queryResult']['parameters']["geo-city"]
    cf=weather(city)
    temp=cf['temp']
    response={
        'fulfillmentText':"Temperature of {} is {}.".format(city,temp)
    }
    print (jsonify(response))
    return jsonify(response)

def weather(city):
    api_key = 'b2ed85bf6e9f00236fa9e63748addba7'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
    source = urllib.request.urlopen(url).read()
    list_of_data = json.loads(source)
    data = {
            "country_code": str(list_of_data['sys']['country']),
            "name": str(list_of_data['name']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
    cf=data
    return cf

