
from Weather_API.Weather_API import *
from Currency_API.Currency_API import *
from Yelp_API.Yelp_API import *
from Database.sql_database import *
from Login_Menu import *
import geonamescache
from Database import *
from getLocation import *

def main():

    login = user_login_menu()
    login_name = login[1]
    login_bool = login[0]
    while (login_bool):
        print (f' \n Welcome {login_name} . Here are your options : \n'
            '1 : Search New Location \n'
            '2 : Disply previous searches \n'
            '3 : Exit Program ' )
        menuChoice = input("Please enter a number. ")

        if menuChoice == '1' :
            api = API
            login = login_name
            location = get_country_and_city()
            yelp = str(Yelp_API(location))
            weather = str(Weather_API(location))
            currency = str(Currency_API(location))
            print (weather,currency,yelp)
            api.add_User_Data(api,login,location,weather,yelp,currency)
        if menuChoice == '2' :
          api = API
          login = login_name
          api.view_User_Data(api, login)
        if menuChoice == '3' :
            print("|-----------------------------------------------------------------|")
            print("| Thanks for using the program!\t\t\t\t\t  |")
            print("|-----------------------------------------------------------------|")
            break
        else :
            print("| Invaild menu choice. Please enter a Number.\t\t\t  |")
            


main()






