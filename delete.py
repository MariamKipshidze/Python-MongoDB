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


my_query = {"address": "Rustavi"}

my_doc = my_col.find(my_query)
for x in my_doc:
    print(x)

# The first parameter of the delete_one() method is a query object defining which document to delete.
my_col.delete_one(my_query)


my_doc = my_col.find(my_query)
for x in my_doc:
    print(x)

# Delete Many Documents
myquery = {"address": {"$regex": "^S"}}

x = my_col.delete_many(myquery)


# Delete All Documents in a Collection
my_col.delete_many({})
