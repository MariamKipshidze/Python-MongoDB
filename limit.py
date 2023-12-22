import pymongo

from local import MONGODB_USERNAME, MONGODB_PASSWORD

# Python MongoDB Limit #

mongo_client = pymongo.MongoClient(
    host="mongodb://localhost:27017/",
    username=MONGODB_USERNAME,
    password=MONGODB_PASSWORD
)

my_db = mongo_client["mongo_database"]
my_col = my_db["customers"]

my_result = my_col.find().limit(1)

# print the result:
for x in my_result:
    print(x)
