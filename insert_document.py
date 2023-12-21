import pymongo

from local import MONGODB_USERNAME, MONGODB_PASSWORD

# Insert Into Collection #

mongo_client = pymongo.MongoClient(
    host="mongodb://localhost:27017/",
    username=MONGODB_USERNAME,
    password=MONGODB_PASSWORD
)

my_db = mongo_client["mongo_database"]
my_col = my_db["customers"]

my_dict = {"name": "Mariam", "address": "Rustavi"}


x = my_col.insert_one(my_dict)

# Return the _id Field #

print(x.inserted_id)

# Insert Multiple Documents #

mylist = [
    {"_id": 1, "name": "name_1", "address": "Rustavi"},
    {"_id": 2, "name": "name_2", "address": "Tbilisi"}
]

x = my_col.insert_many(mylist)
print(x.inserted_ids)
