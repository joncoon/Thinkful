import time
from dateutil.parser import parse
import collections
import sqlite3 as lite
import requests

con = lite.connect('citi_bike.db')
cur = con.cursor()

for i in range(60):
	r = requests.get('http://www.citibikenyc.com/stations/json')
	exec_time = parse(r.json()['executionTime'])

 # Rename Columns and make them lower case
r = r.columns.map(lambda x: x.replace('.', '_').lower())

	cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time.strftime('%s'),))
	con.commit()

	id_bikes = collections.defaultdict(int)
	for station in r.json()['stationBeanList']:
		id_bikes[station['id']] = station['availableBikes']

	for k, v in id_bikes.iteritems():
		cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = " + exec_time.strftime('%s') + ";")
	con.commit()

	time.sleep(60)

con.close() #close the database connection when done

#analyze the result

import pandas as pd
import sqlite3 as lite

con = lite.connect('citi_bike.db')
cur = con.cursor

df = pd.read_sql_query("SELECT * FROM available_bikes ORDER BY execution_time",con,index_col='execution_time')

hour_change = collections.defaultdict(int)
for col in df.columns
	station_vals = df[col].tolist()
	station_id = col[1:] #trims the "_"
	station_change = 0
	for k,v in enumerate(station_vals):
		if k < len(station_vals) - 1:
			station_change += abs(station_vals[k] - station_vals[k+1])
	hour_change[int(station_id)] = station_change # converts the station id back to an integer

def keywithmaxval(d):
	# create a list of the dict' key and value;
	v = list(d.values())
	k = list(d.keys())

	#retur the key with the max value
	return k[v.index(max(v))]

#assign the max key to max_station
max_station = keywithmaxval(hour_change)

#query sqlite for reference information
cur.execute("SELECT id, stationname, latitude, longitude FROM citibike_reference WHERE id = ?", (max_station,))
data = cur.fetchone()
print "The most active station is station id %s at %s latitude: %s longitude: %s " % data
print "With " + str(hour_change[379]) + " bicycles coming and going in the hour between " + datetime.datetime.fromtimestamp(int(df.index[0])).strftime('%Y-%m-%dT%H:%M:%S') + " and " + datetime.datetime.fromtimestamp(int(df.index[-1])).strftime('%Y-%m-%dT%H:%M:%S')