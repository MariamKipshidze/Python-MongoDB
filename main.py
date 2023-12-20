import pymongo

from local import MONGODB_PASSWORD, MONGODB_USERNAME

mongo_client = pymongo.MongoClient(
    host="mongodb://localhost:27017/",
    username=MONGODB_USERNAME,
    password=MONGODB_PASSWORD
)

my_db = mongo_client["mongo_database"]

# Create a collection and insert some data
collection = my_db['my_collection']
data_to_insert = {'test': 'test database'}
collection.insert_one(data_to_insert)

# Check if Database Exists

print(mongo_client.list_database_names())

dblist = mongo_client.list_database_names()
if "mongo_database" in dblist:
    print("The database exists.")
