import sqlite3
import psycopg2

# Using ElephantSQL
dbname = 'zdkyfkhh'
user = 'zdkyfkhh'
password = 'secret'
host = 'salt.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

create_another_titanic_table = """
    CREATE TABLE titanic_table (
        id SERIAL PRIMARY KEY,
        survived INT,
        pclass INT,
        name TEXT,
        sex TEXT,
        age INT,
        siblings_spouses_aboard INT,
        parents_children_aboard INT,
        fare REAL
);
"""
pg_curs.execute(create_another_titanic_table)

# show_tables = """
# SELECT *
# FROM pg_catalog.pg_tables
# WHERE schemaname != 'pg_catalog'
# AND schemaname != 'information_schema';
# """
# pg_curs.execute(show_tables)

sl3_conn = sqlite3.connect('titanic.db')
sl3_curs = sl3_conn.cursor()
titanic = sl3_curs.execute('SELECT * FROM titanic_table;').fetchall()

for i in titanic:
    insert_titanic_row = """
        INSERT INTO titanic_table
        (survived, pclass, name, sex, age, siblings_spouses_aboard, parents_children_aboard, fare)
        VALUES """ + str(i[1:]) + ";"

    pg_curs.execute(insert_titanic_row)

    pg_curs.close()
    pg_conn.commit()