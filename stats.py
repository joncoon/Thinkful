import sqlite3 as lite


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
