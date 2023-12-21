import pymongo

from local import MONGODB_USERNAME, MONGODB_PASSWORD

# Python MongoDB Query #

mongo_client = pymongo.MongoClient(
    host="mongodb://localhost:27017/",
    username=MONGODB_USERNAME,
    password=MONGODB_PASSWORD
)

my_db = mongo_client["mongo_database"]
my_col = my_db["customers"]

# The first argument of the find() method is a query object, and is used to limit the search
myquery = {"address": "Rustavi"}

my_doc = my_col.find(myquery)

for x in my_doc:
    print(x)


# E.g. to find the documents where the "address" field starts with
# the letter "S" or higher (alphabetically), use the greater than modifier: {"$gt": "S"}:
myquery = {"address": {"$gt": "S"}}

my_doc = my_col.find(myquery)

for x in my_doc:
    print(x)

# Filter With Regular Expressions
# To find only the documents where the "address" field starts with the
# letter "S", use the regular expression {"$regex": "^S"}:
myquery = {"address": {"$regex": "^S"}}

my_doc = my_col.find(myquery)

for x in my_doc:
    print(x)
