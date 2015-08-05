
import requests
import sqlite3 as lite
import datetime


apikey = '2e2f577ca9f8eb244e19aa4594cc1744/'

url = 'https://api.forecast.io/forecast/' + apikey

cities = { "San Francisco": '37.727239,-123.032229',
			"Seattle": '47.620499,-122.350876',
			"Philadelphia": '40.009376,-75.133346',
			"Denver": '39.761850,-104.881105',
			"Miami": '25.775163,-80.208615'
		}


#unclear why?

end_date = datetime.datetime.now() # by setting this equal to a variable, we fix the calculation to the point when we started the scrip (rather than have things move aroudn while we're coding.)



con = lite.connect('weather.db')
cur = con.cursor()

cities.keys()
with con:
	cur.execute("DROP TABLE IF EXISTS daily_temp")
	cur.execute('CREATE TABLE daily_temp ( day_of_reading INT, San Francisco REAL, Seattle REAL, Philadelphia REAL, Denver REAL, Miami REAL)')

query_date = end_date - datetime.timedelta(days=30) #the current value being processed

with con:
    while query_date < end_date:
        cur.execute("INSERT INTO daily_temp(day_of_reading) VALUES (?)", (int(query_date.strftime('%s')),))
        query_date += datetime.timedelta(days=1)

for k,v in cities.iteritems():
    query_date = end_date - datetime.timedelta(days=30) #set value each time through the loop of cities
    while query_date < end_date:
        #query for the value
        r = requests.get(url + v + ',' +  query_date.strftime('%Y-%m-%dT12:00:00'))

        with con:
            #insert the temperature max to the database
            cur.execute('UPDATE daily_temp SET ' + k + ' = ' + str(r.json()['daily']['data'][0]['temperatureMax']) + ' WHERE day_of_reading = ' + query_date.strftime('%s'))

        #increment query_date to the next day for next operation of loop
        query_date += datetime.timedelta(days=1) #increment query_date to the next day


con.close() # a good practice to close connection to database

