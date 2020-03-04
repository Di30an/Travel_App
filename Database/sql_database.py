import sqlite3 
# from .config import db  # .config means import from this directory 

# Get datetime info when the user gets a location. Store it in the user class. 
db_path = 'api.db'
db = db_path
class API:
    def __init__(self):
        with sqlite3.connect(db) as conn:
            conn.execute ('CREATE TABLE IF NOT EXISTS User_Data(User_Email TEXT, Weather_API TEXT, YELP_API TEXT, CURRENCY_API TEXT, DATE TEXT)')
            conn.execute ('CREATE TABLE IF NOT EXISTS Users (User_Email TEXT, User_Password) ')
            print("init")

    def add_User_Data (self,User, location, weather,yelp, currency):
        print(User)


        insert_sql = "INSERT INTO User_Data (User_Email, Weather_API, Yelp_API, Currency_API, DATE) VALUES (?,?,?,?,?)" 
        date = ""
        with sqlite3.connect(db) as conn:

            conn.execute(insert_sql, (User, weather, yelp ,currency, date )  )
            print("Success")
        conn.close()
    def view_User_Data(self,User_Email):
        conn = sqlite3.connect(db) 
        sql_view = ('SELECT * FROM User_Data WHERE User_Email = (?)')
        cur = conn.cursor()
        cur.execute(sql_view,(User_Email,) )
        rows = cur.fetchall()
        for row in rows:
            print(row)
        conn.close()
        return 
    def User_Login (self, User_Email, User_Password):
            read_sql = "SELECT User_Email , User_Password FROM Users WHERE User_Email = (?) AND User_Password = (?) "

            with sqlite3.connect(db) as conn :
                c = conn.cursor()
                c.execute (read_sql ,(User_Email,User_Password) )
                all_rows = c.fetchall()

            # Checking if there are any Artwork and returning the proper values.
            if len (all_rows) == 0 :
                print(f'{User_Email} has no profile here.')
            else:
                print("Profile exists")
                return True, User_Email
    
    def create_User(self, User_Email, User_Password):
        insert_sql = "INSERT INTO Users (User_Email, User_Password) VALUES (?,?)" 
        insert_check_sql = " SELECT User_Email FROM Users WHERE User_Email =(?)"

        with sqlite3.connect(db) as conn:
            c = conn.cursor()
            c.execute (insert_check_sql, (User_Email,))
            all_rows = c.fetchall()
            if len (all_rows) > 0:
                print(f'{User_Email} is already in the User database. Account not created. ')
            else : 
                conn.execute(insert_sql, (User_Email, User_Password))
                print(f"Added{User_Email} ")
                return True
        conn.close()

api = API
api.view_User_Data(api,"Has")