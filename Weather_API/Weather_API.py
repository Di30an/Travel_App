#reference to relevant module
import requests
import os
from datetime import datetime , timezone
from Objects.Weather_Obj import Weather


def Weather_API(location):

    key = '816269080b4ebe6ca23ad4449565af85'
    query = {'q' : location.city , 'units' : 'imperial' , 'appid' : key }
    # Url header for api. 
    url = 'http://api.openweathermap.org/data/2.5/weather'
    data = requests.get(url, params= query).json()
    temp = data['main']['temp']
    date = data['dt']
    timedate = datetime.fromtimestamp(date)
    weather = Weather(location.country, location.city, date, temp)

    return weather

