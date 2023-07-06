from pymongo import MongoClient

MONGO_SERVER = 'localhost'
MONGO_PORT = 27017
MONGO_DB = 'gtromortyrick'

client = MongoClient(MONGO_SERVER, MONGO_PORT)
db = client[MONGO_DB]