from Utils.getLocation import get_country_and_city

from Weather_API.Weather_API import *
from Currency_API.Currency_API import *
from Yelp_API.Yelp_API import *

def main():

    location = get_country_and_city()
    weather = Weather_API(location)
    currency = Currency_API(location)
    yelp = Yelp_API(location)

    print (weather,currency,yelp)

    # database_insert(user_name, location, weather, currency, yelp)




main()