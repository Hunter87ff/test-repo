"""this is db module !! """


import server.config as config
from pymongo.asynchronous.mongo_client import AsyncMongoClient


client = AsyncMongoClient(config.DB_URI)
db = client["test_db"]
