from peewee import *
import sqlite3


db = SqliteDatabase('api.db')


class Person(Model) :
    name = Charfield()
    password = CharField()

    class Meta:

        database = db # This model uses the "api.db" databse


class api_results(Model):
    person = ForeignKeyField(Person, backref= 'results')
    name - CharField()
    annimal_type = CharField()

    class Meta:
        database = db # This model uses the "api.db" database


    
