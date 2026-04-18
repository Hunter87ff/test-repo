import os
from bson import ObjectId
from dotenv import load_dotenv
from pymongo import MongoClient
load_dotenv()

DB_URI = os.getenv("DB_URI") 


client = MongoClient(
    DB_URI
)

db = client["test_db"]
users = db.users
# _new_user = users.insert_one(
#     document={
#     "age" : 30,
#     "name" : "Unknown",
#     "email" : "unknown@test.in"
#     }
# )

# _unknown = users.find_one({
#     "age" : 30
# })
# print(_unknown)

# _update_all = users.update_one({
#     "_id" : ObjectId("69e3b209b2ce6854c76d2f8f")
# }, {
#         "$set" :{
#             "email" : "naman@test.in",
#             "name" : "Naman!!"
#         }
# })


# $set = sets a value, update 
# $inc = increments a value, update
# $lte = less than or equal to, query
# $gte = greater than or equal to, query
# $lt = less than, query
# $gt = greater than, query

#print(_update_all.modified_count)

# _all_users = users.find({
#     "age" : {"$lt" : 40}
# })

# for data in _all_users:
#     print(data)


# users.update_many(
#     {"age": {"$lt": 18}},
#     {"$set" : {
#         "minor" : True
#         }
#     }
# )


# _john: dict[str, str] = users.find_one({"name" : "John Doe"}) #type: ignore

# print(_john)


# _rest = users.find(
#     {
#         "age" : {
#             "$lt" : 25
#         }
#     }
# ).to_list(length=None)


# print(_rest)