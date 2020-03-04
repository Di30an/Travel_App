
import unittest 
from unittest import TestCase
from unittest.mock import patch, call

from Weather_API.Weather_API import *
from Currency_API.Currency_API import *
from Yelp_API.Yelp_API import *
from Database.sql_database import *
from Login_Menu import *
import geonamescache
from Database import *
from getLocation import *

Currency_API.Currency_API()
class TestProject4(TestCase):

    """ Mock the print function, check it was called with expected text"""
    @patch('Currency_API.Currency_API')
    def test_dollars_to_target(self,mock_rates):
        mock_rate = 12.3456
        example_api_response = {'base' : 'USD', 'date' : '2019-02-04', 'rates' : {'EUR' : mock_rate}}
        mock_rates.side_effect = [ example_api_response]
if __name__ == '__main__':
    unittest.main()