import pymongo

from local import MONGODB_USERNAME, MONGODB_PASSWORD

# Python MongoDB Update #

mongo_client = pymongo.MongoClient(
    host="mongodb://localhost:27017/",
    username=MONGODB_USERNAME,
    password=MONGODB_PASSWORD
)

my_db = mongo_client["mongo_database"]
my_col = my_db["customers"]

myquery = {"address": "Rustavi"}
new_values = {"$set": {"address": "Tbilisi"}}

my_col.update_one(myquery, new_values)

# print "customers" after the update:
for x in my_col.find():
    print(x)

# Update Many
myquery = {"address": {"$regex": "^S"}}
new_values = {"$set": {"name": "Minnie"}}

my_col.update_many(myquery, new_values)
