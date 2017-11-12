import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.wce
test_collection = db.test_collection

doc = {"name": "cldnjs",
       "school": "dsm"}

test_collection.insert_one(doc)

result = test_collection.find()
for i in result:
    print(i)
