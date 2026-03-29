from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class Sticky(BaseModel):
    channel_id : int
    message : str


_sticky_messages: dict[int, Sticky] = {} #channel_id : Sticky
# _sticky_messages: list[Sticky] = []


@app.post("/sticky")
async def home(req : Request, sticky : Sticky):
    _sticky_messages[sticky.channel_id] =(sticky)
    return {
        "channel" : sticky.channel_id,
        "msg" : sticky.message
    }


@app.get("/sticky/{channel_id}")
async def get_sticky(channel_id : int):

    _sticky = _sticky_messages.get(channel_id)

    if _sticky is None:
        return {
        "status" : "not found"
    }

    return _sticky

    
# @app.delete()
# @app.patch()
# @app.put()
    