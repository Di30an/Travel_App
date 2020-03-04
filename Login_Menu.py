"""
Login is the first window. From there we move to the main menu that allows the user to search 'bookmark' or view bookmarks'
"""
from Database.sql_database import API

def menu():
        print('|-----------------------------------------------------------------|')
        print('| Welcome to Travel App!                                          |\n| If this is your first time you will be asked for your name.     |\n| Then you will enter the country and city that you\'re visiting.  |\n| You will get the local weather, current USD value, &            |\n| the five closest resturants from Yelp with their ratings        |')
        print('|-----------------------------------------------------------------|\n|\t\t\t\t\t\t\t\t  |') 

def user_login_menu():
    menu()
    while True:
        print('|-----------------------------------------------------------------|')
        print('| Welcome to Travel App!                                          |\n| If this is your first time you will be asked for your name.     |\n| Then you will enter the country and city that you\'re visiting.  |\n| You will get the local weather, current USD value, &            |\n| the five closest resturants from Yelp with their ratings        |')
        print('|-----------------------------------------------------------------|\n|\t\t\t\t\t\t\t\t  |')   
        print('| User Login \t\t\t\t\t\t\t  |\n'
        '| 1 : Login \n'
        '| 2 : Add new user\n|')

        menuChoice = input ("| Please enter a number: ")

        if menuChoice == '1':
            email, x = user_login()
            if (x):
                return x
        if menuChoice == '2':
            email, x = add_user()            
            if (x):
                return x
        else:
            print ("| Please enter a menu option: ")


def user_login():
    api = API
    user_email = input("| Enter email: ")
    user_password = input("| Enter password: ")
    result = api.User_Login(api, user_email,user_password)
    return user_email, result

def add_user ():
    api = API
    user_email = input("| Enter email ")
    user_password = input("| Enter password: ")
    result = api.create_User(api, user_email, user_password)
    return user_email, result



