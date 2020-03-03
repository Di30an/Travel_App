
#reference to relevant module
import requests
import os
from datetime import datetime
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
        return 'connection not established!'

def get_country_and_city():
    
    data = get_connection_status()
    country = input('| Enter country: ')
    city = input('| Enter city of choice: ')
    print('|-----------------------------------------------------------------|')
    for i in range(len(data)): 
        value = data[i]['Name']
        if value.lower() == country.lower():
            #return data[i]['Code'] #return country code
            code = data[i]['Code']
            country = data[i]['Name']
            #return city +','+ code
    location_obj = Location(country, city, code)
    return location_obj


