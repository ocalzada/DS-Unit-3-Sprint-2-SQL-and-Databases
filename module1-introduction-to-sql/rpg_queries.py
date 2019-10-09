import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
conn
import os
dir()

curs = conn.cursor()
query1 = 'SELECT COUNT (*) FROM charactercreator_character;'
curs.execute(query1)
curs.fetchall()
# returns total # of characters: 302

def get_result(query):
    curs.execute(query)
    return curs.fetchall()

query2 = 'SELECT COUNT (*) FROM charactercreator_cleric;'
# returns 75 characters in 'cleric'
query3 = 'SELECT COUNT (*) FROM charactercreator_fighter;'
# returns 68 characters in 'fighter'
query4 = 'SELECT COUNT (*) FROM charactercreator_mage;'
# returns 108 characters in 'mage
query5 = 'SELECT COUNT (*) FROM charactercreator_thief;'
# returns 51 characters in 'thief'

query6 = 'SELECT COUNT (*) FROM armory_item;'
# 174 total 'items'

query7 = 'SELECT COUNT (*) FROM armory_item WHERE item_id BETWEEN 138 AND 174;'
# 37 'items' are weapons

query8 = 'SELECT COUNT (*) FROM armory_item WHERE item_id NOT BETWEEN 138 AND 174;'
# 137 'items' are not weapons

query9 = 
'''SELECT ccc.character_id, ccc.name, ccc.exp 
FROM charactercreator_character AS ccc 
INNER JOIN charactercreator_character_inventory as cci 
ON ccc.character_id = cci.item_id LIMIT 20;'''

# - How many Weapons does each character have? (Return first 20 rows)
query10 = 
'''SELECT ccc.character_id, ccc.name, ccc.exp, ai.name, aw.power
 FROM charactercreator_character AS ccc,
 charactercreator_character_inventory AS cci,
 armory_item AS ai, armory_weapon AS aw
 WHERE ccc.character_id = cci.character_id
 AND cci.item_id = ai.item_id
 AND ai.item_id = aw.item_ptr_id
 LIMIT 20;'''
Code above conducts an implicit join among four tables.
Returns all the weapons for each characters
Theres a total of 203 weapons.

# - On average, how many Items does each Character have?
898 items / 174 characters = 5 items/characters

# - On average, how many Weapons does each character have?
203 weapons / 174 characters = ~1 weapon/character

curs.close()
conn.commit()
