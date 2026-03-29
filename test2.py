import requests

_response = requests.post(
    "http://localhost:8000/sticky",
    json={
        "channel_id" : 1480240549264101615,
        "message" : "hello there !!"
    }
)


print(_response.json())
print(_response.text)