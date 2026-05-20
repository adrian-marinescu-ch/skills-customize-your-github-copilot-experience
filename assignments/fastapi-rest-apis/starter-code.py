from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

app = FastAPI(title="FastAPI REST API Starter")

items: List[Item] = [
    Item(id=1, name="Backpack", description="School backpack with extra pockets", price=29.99),
    Item(id=2, name="Notebook", description="Ruled notebook for notes", price=4.50),
]


def find_item(item_id: int) -> Optional[Item]:
    return next((item for item in items if item.id == item_id), None)


@app.get("/items", response_model=List[Item])
async def list_items():
    return items


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    item = find_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items", response_model=Item, status_code=201)
async def create_item(item: Item):
    if find_item(item.id) is not None:
        raise HTTPException(status_code=400, detail="Item ID already exists")
    items.append(item)
    return item


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated_item: Item):
    item = find_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    item.name = updated_item.name
    item.description = updated_item.description
    item.price = updated_item.price
    item.in_stock = updated_item.in_stock
    return item


@app.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: int):
    item = find_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    items.remove(item)


# Run this app with:
#   uvicorn starter-code:app --reload
