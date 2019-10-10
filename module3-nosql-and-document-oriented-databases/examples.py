def increment(x):
    return x + 1

def double(x):
    return x * 2

def run_twice(func, arg):
    return func(func(arg))

#how to print out list using recursion instead
def rec_print(n):
    print(n)
    if n>0:
        rec_print(n-1)

def add(x,y):
    return x + y

def identity(x):
    return x

MONGODB credentials
username = Admin
password = blDzscb7iIJg8Skd

# full driver from mongo
client = pymongo.MongoClient("mongodb://admin:blDzscb7iIJg8Skd@cluster0-shard-00-00-zukxc.mongodb.net:27017,cluster0-shard-00-01-zukxc.mongodb.net:27017,cluster0-shard-00-02-zukxc.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

# check how many machines (3)
client.nodes

#taking a look at db
db

# taking a look at the help function of db 
help(db)

# checking out the directory of db.test
dir(db.test)

#checking out documentation for insert_one method
help(db.test.insert_one)

#insert one document into mongoDB
db.test.insert_one({'x': 1})

# count how many documents
db.test.count_documents({'x':1})

# insert another document
db.test.insert_one({'x': 1})

# count how many documents now
db.test.count_documents({'x':1})

# find one document
db.test.find_one({'x':1})

# 'find' method creates a cursor in mongoDB 
db.test.find({'x':1})

# instantiate the cursor
curs = db.test.find({'x':1})

# create a few documents
anthony_doc = {
    'favorite_animal' : ['leafy sea dragon', 'dragon']
}

rudy_doc = {
    'favorite_animal' : 'Koala',
    'favorite_color' : 'Blue'
}

coop_doc = {
    'favorite_animal' : 'Pangolin'
}

# inser the many documents above into mongoDB
db.test.insert_many([anthony_doc, rudy_doc, coop_doc])

# obtain a list of documents in mongoDB using find() method
list(db.test.find())

# now we make more docs
more_docs = []
for i in range(10):
    doc = {'even': i % 2 == 0}
    doc['value'] = i
    more_docs.append(doc)

# check more_docs has been saved
more_docs

# insert many_docs into mongoDB
db.test.insert_many(more_docs)

# get a list where 'even': False
list(db.test.find({'even':False}))

# Update a single document matching the filter
help(db.test.update_one)

# Delete a single document matching the filter
help(db.test.delete_one)

# update one document matching the filter 'value':3, by increasing it by 'value':5
db.test.update_one({'value':3},{'$inc': {'value':5}})

# get a list of documents in mongoDB
list(db.test.find())

# update many documents matching the filter 'even':True, by increasing it by 'value':100
db.test.update_many({'even':True}, {'$inc': {'value':100}})

# use find() method to make sure our update above worked
list(db.test.find({'even':True}))

# delete many files matching the filter 'even':False
db.test.delete_many({'even':False})

# confirm deletion above worked
list(db.test.find())

#create an rpg character
rpg_character = (1, "King Bob", 10, 3, 0, 0, 0)

#remember to wrap it in a dictionary so that we can insert it
db.test.insert_one({'rpg_character':rpg_character})

# insert one document for one character
db.test.insert_one({
    'sql_id': rpg_character[0],
    'name': rpg_character[1],
    'hp': rpg_character[2],
    'level': rpg_character[3]
})

sl3_conn = sqlite3.connect('rpg_db.sqlite3')
sl3_curs = sl3_conn.cursor()
characters = sl3_curs.execute('SELECT * FROM charactercreator_character;').fetchall()

for i in characters:
    db.test.insert_one({
    'id': i[0],
    'name': i[1],
    'level': i[2],
    'exp': i[3],
    'hp': i[4],
    'strength': i[5],
    'intelligence': i[6],
    'dexterity': i[7],
    'wisdom': i[8]
})

# Uploading instances on MongoDB was easier than PostgreSQL. It's not as organized or neat as ElephantSQl, 
# but it's a great way to upload tables as documents, and then manage/update/delete those 
# documents at a high-level. Another observation, is that seems more difficult to perform data queries 
# in MongoDB as well.