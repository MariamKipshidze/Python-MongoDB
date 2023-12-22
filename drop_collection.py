import pymongo

from local import MONGODB_USERNAME, MONGODB_PASSWORD

# Python MongoDB Delete Document #

mongo_client = pymongo.MongoClient(
    host="mongodb://localhost:27017/",
    username=MONGODB_USERNAME,
    password=MONGODB_PASSWORD
)

my_db = mongo_client["mongo_database"]
my_col = my_db["customers"]

my_col.drop()
