
#reference to relevant module
import requests
import os

import geonamescache
from Objects.Weather_Obj import Weather
from Objects.Location_Obj import Location

''' 
function to get country extension code. 
consume API with list of countries and corresponding codes
'''
def get_connection_status():
    #list of countries and code's API url
    url ='https://pkgstore.datahub.io/core/country-list/data_json/data/8c458f2d15d9f2119654b29ede6e45b8/data_json.json'
    data = requests.get(url) # fetched data stored in JSON format
    if data.status_code == 200:
        data = data.json()
        return data
    elif data.status_code == 404:
        return '| Connection not established!'

#def get_country_and_city():
    
    data = get_connection_status()
    country = input('Enter country: ')
    city = input('Enter city of choice: ')
    for i in range(len(data)): 
        value = data[i]['Name']
        if value.lower() == country.lower():
            #return data[i]['Code'] #return country code
            code = data[i]['Code']
            country = data[i]['Name']
            #return city +','+ code
    location_obj = Location(country, city, code)
    return location_obj

def get_country_and_city():
    country = isCountry()    
    city = isCity(country)
    return city

def isCity(country):
    city = ""
    while True:  
        # Creates a geonamescache object
        gc = geonamescache.GeonamesCache()
        # Makes sure the first letter is uppper case
        city = city.capitalize()
        # Searches geocache libary for city name, returns a dictonary
        city_list = gc.get_cities_by_name('%s' % city) 
        # Use len to find if city exists
        for city in city_list:
            code = list(city.keys())[0]
            county_code = (city[code]['countrycode']) # THIS WORKS!!!!!
            print(county_code)    
            city = (city[code]['name']) # THIS WORKS!!!!!
            location = Location(country, city, county_code)
            return (location)
            
        else:
            city = input('| Please enter a city name: ')

def isCountry():
    # Confirms a countries existance. 
    country = ""
    while True:
        # Creates a geonamescache object
        gc = geonamescache.GeonamesCache()
        # Makes sure the first letter is uppper case
        country = country.capitalize()
        # Searches geocache libary for country, returns a dictonary
        country_list = gc.get_countries_by_names()
        # If country name is found then it returns a country name. 
        for countries in country_list.keys():
            if countries == country :
                return country
        else :
            country = input('| Please enter a country name: ')
#isCity("Spain")