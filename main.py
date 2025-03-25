from fastapi import FastAPI

app = FastAPI()

employees = [
    {"id":111,"name":"Ram","place":"USA"},
    {"id":112,"name":"Krish","place":"UK"},
    {"id":113,"name":"Shiva","place":"India"},
    {"id":114,"name":"Shakti","place":"Chennai"},
    {"id":115,"name":"Steffi","place":"TN"}
]

@app.get('/')
async def hello_world():
    return {"Hello": "Study Corner"}

# Path Parameter
@app.get("/display/{name}")
def viewForPath(name:str):
    for employee in employees:
        if employee['name'] == name:
            return employee

# Query Parameter
@app.get("/display")
def viewForQuery(id:int):
    for employee in employees:
        if employee['id'] == id:
            return employee
        
        
from typing import Optional

# Path Parameter
@app.get("/component/{component_id}")
async def get_component(component_id:int):
    return {"component_id":component_id}

#Query Parameter
@app.get("/component/")
async def read_component(component_id:int, text:Optional[str]):
    return {"component_id":component_id,"text":text}
