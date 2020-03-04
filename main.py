
from Weather_API.Weather_API import *
from Currency_API.Currency_API import *
from Yelp_API.Yelp_API import *
from Database.sql_database import *
from Login_Menu import *
import geonamescache
from Database import *
from getLocation import *

def main():
<<<<<<< HEAD
    login = user_login_menu()
    while (login[0]):
        print (f' \n Welcome {login[1]} . Here are your options : \n'
            '1 : Search New Location \n'
            '2 : Disply previous searches \n'
            '3 : Exit Program ' )
        menuChoice = input("Please enter a number. ")

        if menuChoice == '1' :
            api = API
            login = login[1]
            location = get_country_and_city()

            yelp = str(Yelp_API(location))
            weather = str(Weather_API(location))
            currency = str(Currency_API(location))
 
            api.add_User_Data(api,login,location,weather,yelp,currency)
        if menuChoice == '2' :
          api = API
          login = login[1]
          api.view_User_Data(api, login)
        if menuChoice == '3' :
            print("Thanks for using the program! ")
            break
        else :
            print("Invaild menu choice. Please enter a Number.")
            


main()

=======
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
>>>>>>> Formatting
