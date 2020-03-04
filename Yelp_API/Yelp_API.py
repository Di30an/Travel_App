import requests
import json
import pprint

from Objects.Yelp_Obj import Yelp


def Yelp_API(location):
    # Define the API Key and define the Endpoint and define the Header
    api_key ='ElcFaBRSEjtgHhOeSriUTtk4-jzvJSwZy3DuGPcItCdvb7CPGIX6mAskxI5jWVL6eldFiZfnydTNzf3PDE5wGGgAsdvalWNIjszg5zAKwgvRjnu_5yaIRa7A8tpaXnYx'
    ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
    HEADERS = {'Authorization' : 'Bearer %s' %  api_key}

    # Define the parameters
    PARAMETERS = {'term':'food',
                'limit': 5,
                'radius' : 1000,
                'location': '%s' % location.city}

    # Make a 
    reponse = requests.get(url = ENDPOINT, params= PARAMETERS, headers = HEADERS)


    # Convert the JSON string to a Dictionary
    business_data = reponse.json()

    # Returns the name rating and the zip code for the 5 closest resturants

    yelp_data = []
    count = 1 #formatting resturant count, CR
    for biz in business_data['businesses']:
        countStr = str(count) #convert biz count, CR
        biz_data = (countStr, biz['name'], biz ['rating'], biz['location']['country'])
        yelp_data.append(biz_data)
        count += 1
    yelp_data = Yelp (location.country, location.city , yelp_data)
    return yelp_data