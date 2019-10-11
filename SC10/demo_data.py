import sqlite3

# PART ONE
# create and establish new connection with sqlite3 DB.
sl3_conn = sqlite3.connect('demo_data.sqlite3')

#instantiate connection cursor
sl3_curs = sl3_conn.cursor()

# create 'demo table' variable
create_demo_table = """
    CREATE TABLE demo (
        id SERIAL PRIMARY KEY,
        s TEXT,
        x INT,
        y INT
);
"""
#execute create table variable
sl3_curs.execute(create_demo_table)

# create 'insert into demo' table variable
insert_demo_data = """
        INSERT INTO demo
        (s, x, y)
        VALUES ('g', 3, 9), ('v', 5, 7), ('f', 8, 7);
"""
# execute and insert demo data into demo table
sl3_curs.execute(insert_demo_data)

# close cursor and commit data insertion into demo table
sl3_curs.close()
sl3_conn.commit()

# open cursor again
sl3_curs = sl3_conn.cursor()

# Q1: Count how many rows you have - it should be 3!

# execute SQL query getting all rows in our table
sl3_curs.execute('SELECT COUNT (*) FROM demo;')
# fetch SQL query
sl3_curs.fetchall()
# number of rows count:
[(3,)]

# Q2: How many rows are there where both x and y are at least 5?
sl3_curs.execute('SELECT COUNT (*) FROM demo WHERE x >= 5 AND y >=5;')
sl3_curs.fetchall()
# number of rows where both x and y are >= 5:
[(2,)]

# Q3: How many unique values of y are there?
l3_curs.execute('SELECT COUNT(DISTINCT y) FROM demo;')
sl3_curs.fetchall()
# unique values of y:
[(2,)]
