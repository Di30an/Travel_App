import requests
# A python module for currencies. See https://pypi.org/project/ccy/
import ccy
from Objects.Currency_Obj import *

def Currency_API(location):
    # No API Key required.
    # Retrives the country code from the yelp data
    # Using the ccy module to conver the country code to a currency code.
    country_currency = ccy.countryccy(location.country_code)
    # Make a request
    reponse = requests.get('https://api.exchangeratesapi.io/latest?base=USD')
    business_data = reponse.json()
    country_exchange_rate = (business_data['rates'][country_currency])
    currency_data = Currency(location.country,country_currency, country_exchange_rate)
    return currency_data


