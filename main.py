from typing import Optional
from fastapi import FastAPI

from pydantic import BaseModel

class Package(BaseModel):
    name: str
    number: str
    description: Optional[str] = None

app = FastAPI()

# Pydantic's BaseModel

@app.get('/')
async def hello_world():
    return {'Hello' : 'World'}

@app.post("/package/{priority}")
async def make_package(priority: int, package: Package, value: bool):
    return {"priority": priority, **package.dict(), "value": value}





class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None




@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict