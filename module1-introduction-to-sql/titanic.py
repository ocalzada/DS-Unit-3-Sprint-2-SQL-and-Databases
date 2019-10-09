# this is all done in python3

import sqlite3
import pandas as pd

# read titanic.csv as pandas dataframe
df = pd.read_csv('titanic.csv')

# create connection with new sqlite database
sl3_conn = sqlite3.connect('titanic.db')

# write records stored in a dataframe to a SQL database
df.to_sql('titanic_table', sl3_conn)

# instantiate connection cursor
sl3_curs = sl3_conn.cursor()

# execute query using cursor instantiation
sl3_curs.execute('SELECT * FROM titanic_table;')

# get query results
sl3_curs.fetchall()

# close cursor
sl3_curs.close()

# commit queries
sl3_conn.commit()