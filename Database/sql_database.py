import sqlite3 
# from .config import db  # .config means import from this directory 
from .config import db_path

db = db_path
class API:
    def __init__(self):
        with sqlite3.connect(db) as con : 
           con.execute('CREATE TABLE IF NOT EXISTS YELP (USERNAME TEXT UNIQUE NOT NULL, RESTURANTS TEXT)')
           con.execute('CREATE TABLE IF NOT EXISTS YELP (USERNAME TEXT UNIQUE NOT NULL, RESTURANTS TEXT)')