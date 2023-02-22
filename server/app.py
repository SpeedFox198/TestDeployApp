from quart import Quart
from quart_cors import cors

app = Quart(__name__)
app = cors(app, allow_credentials=True, allow_origin=["https://localhost"])


@app.get("/")
async def home():
    return "I exist ok?"


@app.get("/2")
async def two():
    return {"two": 2}
