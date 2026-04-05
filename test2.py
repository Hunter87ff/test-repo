import os
from dotenv import load_dotenv
from pymongo import MongoClient
load_dotenv()

DB_URI = os.getenv("DB_URI") 


client = MongoClient(
    DB_URI
)

db = client["test_db"]
users = db["users"]
# _new_user = await users.insert_one(
#     document={
#     "name" : "Unknown",
#     "email" : "unknown@test.in"
#     }
# )

# _unknown = users.find_one({"name" : "Unknown"})
# print(_unknown)

# _update_all = users.update_many({}, {
    #     "$set" :{
    #         "age" : 1,
    #     }
    # })

#print(_update_all.modified_count)

# _all_users = users.find({"name" : "Unknown"}).to_list(length=None)
# print(_all_users)


# users.update_one({"name" : "John Doe"}, {"$set": {"age": 25}})
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