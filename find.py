import pymongo

from local import MONGODB_USERNAME, MONGODB_PASSWORD

# Python MongoDB Find #

mongo_client = pymongo.MongoClient(
    host="mongodb://localhost:27017/",
    username=MONGODB_USERNAME,
    password=MONGODB_PASSWORD
)

mydb = mongo_client["mongo_database"]
my_col = mydb["customers"]

# The find_one() method returns the first occurrence in the selection
x = my_col.find_one()
print(x)

print("--------------------------------------------------")

# The first parameter of the find() method is a query object. In this example we use an
# empty query object, which selects all documents in the collection.
for x in my_col.find():
    print(x)

print("--------------------------------------------------")

# Return Only Some Fields
# Return only the names and addresses, not the _ids
for x in my_col.find({}, {"_id": 0, "name": 1, "address": 1}):
    print(x)
