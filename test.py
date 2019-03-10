from pymongo import MongoClient
from bson import ObjectId
dbName = "aggregation"
client = MongoClient('mongodb://localhost:27017/')
db = client[dbName]