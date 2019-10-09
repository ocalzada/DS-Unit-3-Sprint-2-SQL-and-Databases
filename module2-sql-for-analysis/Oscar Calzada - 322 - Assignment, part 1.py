#Installing psycopg2
!pip install psycopg2-binary

#importing libraries
import psycopg2
import sqlite3

# reviewing options from directory and help documentation
dir(psycopg2)
help(psycopg2.connect)

# Connection info from Elephant SQL
dbname = 'zdkyfkhh'
user = 'zdkyfkhh'
password = 'secret'
host = 'salt.db.elephantsql.com'

#creating the connection object using our credentials above
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

#verifying our connection object was created
pg_conn

#creating the cursor object which allows us to interact with DB
pg_curs = pg_conn.cursor()

# example query to select all from the test_table we had previously created in ElephantSQL
pg_curs.execute('SELECT * FROM test_table;')
pg_curs.fetchall()

# getting the rpg database file from github
!wget https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/rpg_db.sqlite3?raw=true

!ls -alh

# relabeling the rpg database
!mv 'rpg_db.sqlite3?raw=true' rpg_db.sqlite3

# creating a connection object with our sqlite3 db
s1_conn = sqlite3.connect('rpg_db.sqlite3')

# creating a cursor to interact with sqlite3 db
s1_curs = s1_conn.cursor()

# sqlite3 query example
s1_curs.execute('SELECT COUNT (DISTINCT name) FROM charactercreator_character').fetchall()

# instantiating the sqlite3 query to a variable
characters = s1_curs.execute('SELECT * FROM charactercreator_character;').fetchall()

# taking a look at the entries
characters[0]

characters[-1]

len(characters)

# obtaining the table schema from the sqlite3 db
s1_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall()

# used the table schema info to 'create table' query
create_character_table = """
  CREATE TABLE charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name varchar(30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT
  );
"""
# executing 'create table' query in ElephantSQL
pg_curs.execute(create_character_table)

# creating 'show table' query
show_tables = """
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""
# executing 'show table' query in ElephantSQL
pg_curs.execute(show_tables)

# getting the results of the execution
pg_curs.fetchall()

# example of first entry
characters[0]

# converting first entry into a string & splicing the first column
str(characters[0][1:])

# creating an 'insert into' query example
example_insert = """
INSERT INTO charactercreator_character
(name, level, exp, hp, strength, intelligence, dexterity, wisdom)
VALUES """ + str(characters[0][1:]) + ';'

# printing that example query
print(example_insert)

# creating a for loop for each character in characters list 
# AND executing query into ElephantSQL
for character in characters:
  insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ';'
    # print(insert_character)
  pg_curs.execute(insert_character)

# executing query for contents of the 'charactercreator_character' table
# we created & just filled in ElephantSQL
pg_curs.execute('SELECT * FROM charactercreator_character;')

pg_curs.fetchall()

# closing cursor
pg_curs.close()

# commiting changes
pg_conn.commit()

#making sure our connection is still live
pg_conn

#reopening cursor to check for errors
pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM charactercreator_character;')
pg_characters = pg_curs.fetchall()

# first row in sqlite3
characters[0]

# first row in ElephantSQL
pg_characters[0]

# verifying entries were copied correctly, use 'assert' function
for character, pg_character in zip(characters,pg_characters):
  assert character == pg_character