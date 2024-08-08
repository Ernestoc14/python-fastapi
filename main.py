from typing import Union
from fastapi import FastAPI

# fastapi dev main.py
app = FastAPI()

@app.get("/")
def read_root():
    return {"Fast Api is Running"}


@app.get("/items/{item_id}")
def read_item(item_id: int, quote: Union[str, None] = None):
    return {"item_id": item_id, "quote": quote}