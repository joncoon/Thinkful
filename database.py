'''
Write a script called "database.py" to print out the cities with the July being the warmest month. Your script must:
Connect to the database
Create the cities and weather tables (HINT: first pass the statement DROP TABLE IF EXISTS <table_name>; to remove the table before you execute the CREATE TABLE ... statement)
Insert data into the two tables
Join the data together
Load into a pandas DataFrame
Print out the resulting city and state in a full sentence. For example: "The cities that are warmest in July are: Las Vegas, NV, Atlanta, GA..."
'''

import sqlite3 as lite
import pandas as pandas
import sys

print "This code will print out cities with a given month being the warmest"

month = raw_input("Which month are you interested in ")

print month

con = lite.connect('getting_started.db')

cities = (
    ('New York City', 'NY')
    ('Boston', 'MA'),
    ('Chicago', 'IL'),
    ('Miami', 'FL'),
    ('Dallas', 'TX'),
    ('Seattle', 'WA'),
    ('Portland', 'OR'),
    ('San Francisco','CA'),
    ('Los Angeles', 'CA')
)

weather = (
    ('New York City', 2013, 'July', 'January', 62),
    ('Boston', 2013, 'July', 'January', 59),
    ('Chicago', 2013, 'July','January', 59),
    ('Miami', 2013, 'August', 'January', 84),
    ('Dallas', 2013, 'July', 'January', 77),
    ('Seattle', 2013, 'July', 'January', 61),
    ('Portland', 2013, 'July', 'December', 63),
    ('San Francisco', 2013, 'September', 'December', 64),
    ('Los Angeles', 2013, 'September', 'December', 75)
)

def populate(connection):

    # Inserting rows by passing values directly to `execute()`
    with connection as con:

        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS cities")
        cur.execute("DROP TABLE IF EXISTS weather")

        cur.execute("CREATE TABLE cities (name text, state text)")
        cur.execute(
        	"CREATE TABLE weather (\
        		city text, \
        		year integer, \
        		warm_month text, \
        		cold_month text, \
        		average_high integer)"
        	)

        cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
        cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)

print "The cities that are warmest in July are: ",