# import typing
from server.db import db



class User:
    _collection = db.users

    def __init__(self, payload: dict):
        self.name = payload.get("name")
        self.email = payload.get("email")
        self.password = payload.get("password")

    async def save(self):
        _data = {
            "name": self.name,
            "email": self.email,
            "password": self.password
        }
        
        await self._collection.update_one(
            {"email": self.email},
            {"$set": _data},
            upsert=True
        )

        

    

