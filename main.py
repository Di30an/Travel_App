from Utils.getLocation import get_country_and_city

from Weather_API.Weather_API import *
from Currency_API.Currency_API import *
from Yelp_API.Yelp_API import *

def main():
    print('|-----------------------------------------------------------------|')
    print('| Welcome to Travel App!                                          |\n| If this is your first time you will be asked for your name.     |\n| Then you will enter the country and city that you\'re visiting.  |\n| You will get the local weather, current USD value, &            |\n| the five closest resturants from Yelp with their ratings        |')
    print('|-----------------------------------------------------------------|\n|\t\t\t\t\t\t\t\t  |')
    location = get_country_and_city()
    weather = Weather_API(location)
    currency = Currency_API(location)
    yelp = Yelp_API(location)

    print (weather,currency,yelp)
    

    # database_insert(user_name, location, weather, currency, yelp)




main()