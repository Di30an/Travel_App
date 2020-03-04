"""
Login is the first window. From there we move to the main menu that allows the user to search 'bookmark' or view bookmarks'
"""
from Database.sql_database import API

        

def user_login_menu():
    while True:
        print('User Login \n'
        '1 : Login \n'
        '2 : Add new user')

        menuChoice = input ("Please enter a number. ")

        if menuChoice == '1':
            email, x = user_login()
            if (x):
                return x
        if menuChoice == '2':
            email, x = add_user()            
            if (x):
                return x
        else:
            print ("Please enter a menu option ")


def user_login():
    api = API
    user_email = input("Enter email ")
    user_password = input("Enter password")
    result = api.User_Login(api, user_email,user_password)
    return user_email, result

def add_user ():
    api = API
    user_email = input("Enter email ")
    user_password = input("Enter password")
    result = api.create_User(api, user_email, user_password)
    return user_email, result



