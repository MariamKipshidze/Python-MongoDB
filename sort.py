import pymongo

from local import MONGODB_USERNAME, MONGODB_PASSWORD

# Python MongoDB Sort #

mongo_client = pymongo.MongoClient(
    host="mongodb://localhost:27017/",
    username=MONGODB_USERNAME,
    password=MONGODB_PASSWORD
)

my_db = mongo_client["mongo_database"]
my_col = my_db["customers"]

# sort("name", 1) #ascending
# sort("name", -1) #descending
my_doc = my_col.find().sort("name", -1)

for x in my_doc:
    print(x)
