from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
import first_lab as FL

class Item_3(BaseModel):
    value: list

class Item(BaseModel):
    name: str
    description: Union[str,None] = None
    price: float
    tax: Union[float,None] = None

class Ten_Schema(BaseModel):
    """
    A*x*x + B*x + C = 0
    """
    A:float
    B:float
    C:float
    complex:bool

def item_to_dic(item:Item) -> dict:
    return {'name':item.name,'description':item.description,'price':item.price,'tax':item.tax}

app = FastAPI()

@app.get("/first/{item_val}")
def One(item_val: bool):
    return {"first result":FL.first(item_val)}
    
@app.get("/second/{item_val}")
def Two(item_val: str):
    return {"second result":FL.second(item_val)}

@app.post("/third/")
async def Third(item_val: Item_3):
    item_list = item_val.value
    return {"third result":FL.third(item_list)}

@app.get("/four/{item_val}")
def Four(item_val: int):
    return {"four result":FL.forth(item_val)}

@app.get("/five/{item_val}")
def Five(item_val: str):
    return {"five result":FL.fifth(item_val)}

@app.get("/six/{item_val}")
def Six(item_val: str):
    return {"six result":FL.six(item_val)}

@app.get("/seven/{item_val}")
def Seven(item_val: int):
    return {"seven result":FL.seven(item_val)}

@app.post("/eight/")
async def Eight(item_val: Item_3):
    item_list = item_val.value
    return {"eight result":FL.eight(item_list)}

@app.post("/ten/")
async def Ten(item: Ten_Schema):
    res = FL.solve_ten(item.A,item.B,item.C,item.complex)
    return res