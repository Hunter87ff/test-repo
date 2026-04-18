
from fastapi import FastAPI, Request
from pydantic import BaseModel



app = FastAPI()


class Userr:
    id : int
    name : str
    email : str
    perms : list[int]

class User(BaseModel):
    name : str
    email : str

__users: dict[str, User] = {} #channel_id : Sticky

@app.post("/users")
async def create_user(req : Request, user : User):
    
    _existing = __users.get(user.email)

    if _existing:
        return {
            "status" : "already exists"
        }

    __users[user.email] = user
    print(user)
    return {
        "name" : user.name,
        "email" : user.email,
        "roles" : ["user"]
    }


@app.get("/users/{email}")
async def get_user(email : str):
    _user = __users.get(email)
    if _user is None:
        return {
        "status" : "not found"
    }

    return _user


@app.patch("/users/{email}")
async def update_user(email : str, user : User):
    _existing = __users.get(email)
    if _existing is None:
        return {
            "status" : "not found"
        }

    if _existing.email != user.email:
        __users.pop(email)
        __users[user.email] = user

    else:  
        __users[email] = user

    return {
        "status" : "updated",
        "user" : user
    }

@app.delete("/users/{email}")
async def delete_user(email : str):
    _user = __users.pop(email, None)
    if _user is None:
        return {
            "status" : "not found"
        }
    return {
        "status" : "deleted",
        "user" : _user
    }