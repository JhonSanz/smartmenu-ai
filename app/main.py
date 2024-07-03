from typing import Union, Any

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


class ItemOut(BaseModel):
    item_name: str
    item_id: int


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}", response_model=ItemOut)
def update_item(item_id: int, item: Item) -> Any:
    return {"item_name": item.name, "item_id": item_id}
