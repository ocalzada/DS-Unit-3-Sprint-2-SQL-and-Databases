import sqlite3

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()
curs.execute('SELECT COUNT(sports) FROM "buddymove_holidayiq.sqlite3"')
curs.fetchall()
# query test returns 249 rows!

curs.execute('SELECT COUNT(nature), COUNT(shopping) 
            FROM "buddymove_holidayiq.sqlite3" 
            WHERE nature >= 100 AND shopping >= 100;')

curs.fetchall()
# query test returns 78 rows, corresponding to the
# number of users who reviewed at least 100 Nature
# and 100 shopping categories.